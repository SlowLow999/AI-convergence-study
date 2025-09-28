#!/usr/bin/env python3
"""
Simple Data Loader for AI Model Convergence Research
Load and explore the research data in a user-friendly way.
"""

import json
from pathlib import Path

def load_research_data(file_path="data/ai_research_data.json"):
    """Load the research data from JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {file_path}")
        print("Make sure the data file is in the correct location!")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}")
        return None

def print_experiment_summary(data, experiment_name):
    """Print a summary of a specific experiment."""
    exp = data['experiments'][experiment_name]
    analysis = exp['analysis']
    
    print(f"\n{'='*60}")
    print(f"EXPERIMENT: {experiment_name.upper().replace('_', ' ')}")
    print(f"{'='*60}")
    print(f"Prompt: '{exp['prompt']}'")
    print(f"Total Models: {exp['total_models']}")
    
    if experiment_name == 'joke_generation':
        # Special handling for jokes
        print(f"Top Response: {analysis['joke_categories'][0]['category']}")
        print(f"Convergence: {analysis['joke_categories'][0]['percentage']:.1f}%")
    elif experiment_name == 'color_selection':
        # Special handling for colors
        print(f"Top Response: {analysis['top_choice']}")
        print(f"Convergence: {analysis['top_choice_percentage']:.1f}%")
    else:
        # Default handling
        print(f"Top Response: '{analysis['top_response']}'")
        print(f"Convergence: {analysis['top_response_percentage']:.1f}%")
    
    print(f"Unique Responses: {analysis.get('unique_responses', analysis.get('unique_jokes', analysis.get('unique_colors', 'N/A')))}")
    print(f"Diversity Index: {analysis['diversity_index']:.1f}%")

def print_top_responses(data, experiment_name, n=5):
    """Print the top N responses for an experiment."""
    exp = data['experiments'][experiment_name]
    
    print(f"\nTop {n} Responses:")
    print("-" * 40)
    
    if experiment_name == 'joke_generation':
        categories = exp['analysis']['joke_categories'][:n]
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat['category']}: {cat['count']} models ({cat['percentage']:.1f}%)")
            print(f"   Example: \"{cat['joke']}\"")
    elif experiment_name == 'color_selection':
        colors = exp['analysis']['color_distribution'][:n]
        for i, color in enumerate(colors, 1):
            print(f"{i}. {color['color']}: {color['count']} models ({color['percentage']:.1f}%)")
    else:
        # For random words, we need to count from responses
        from collections import Counter
        word_counts = Counter()
        for response in exp['responses']:
            word_counts[response['response']] += 1
        
        for i, (word, count) in enumerate(word_counts.most_common(n), 1):
            percentage = (count / exp['total_models']) * 100
            print(f"{i}. '{word}': {count} models ({percentage:.1f}%)")

def main():
    """Main function to demonstrate data loading and exploration."""
    print("AI Model Convergence Research - Data Loader")
    print("=" * 50)
    
    # Load the data
    data = load_research_data()
    if not data:
        return
    
    # Print study metadata
    metadata = data['study_metadata']
    print(f"Study: {metadata['title']}")
    print(f"Total Experiments: {metadata['total_experiments']}")
    print(f"Date: {metadata['date_conducted']}")
    
    # Print summary for each experiment
    experiments = ['random_word_generation', 'joke_generation', 'color_selection']
    
    for exp_name in experiments:
        print_experiment_summary(data, exp_name)
        print_top_responses(data, exp_name)
    
    # Print comparative analysis
    print(f"\n{'='*60}")
    print("COMPARATIVE ANALYSIS")
    print(f"{'='*60}")
    
    comp_analysis = data['comparative_analysis']['convergence_ranking']
    print("\nConvergence Ranking (highest to lowest):")
    for i, exp in enumerate(comp_analysis, 1):
        print(f"{i}. {exp['experiment']}: {exp['convergence_rate']:.1f}% on '{exp['top_choice']}'")
    
    print("\nKey Findings:")
    for finding in data['comparative_analysis']['key_findings']:
        print(f"• {finding}")

if __name__ == "__main__":
    main()
