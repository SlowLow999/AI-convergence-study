#!/usr/bin/env python3
"""
Advanced Analysis Script for AI Model Convergence Research
Automated analysis with visualizations and statistical insights.
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from collections import Counter
from pathlib import Path

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_data(file_path="data/ai_research_data.json"):
    """Load research data from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_convergence_patterns(data):
    """Analyze convergence patterns across all experiments."""
    experiments = data['experiments']
    results = []
    
    for exp_name, exp_data in experiments.items():
        analysis = exp_data['analysis']
        
        if exp_name == 'joke_generation':
            top_rate = analysis['joke_categories'][0]['percentage']
        elif exp_name == 'color_selection':
            top_rate = analysis['top_choice_percentage']
        else:
            top_rate = analysis['top_response_percentage']
        
        results.append({
            'experiment': exp_name.replace('_', ' ').title(),
            'convergence_rate': top_rate,
            'diversity_index': analysis['diversity_index'],
            'total_models': exp_data['total_models']
        })
    
    return pd.DataFrame(results)

def analyze_model_families(data):
    """Analyze response patterns by model family."""
    model_families = {
        'claude': [],
        'gpt': [],
        'gemini': [],
        'llama': [],
        'qwen': [],
        'other': []
    }
    
    # Process each experiment
    for exp_name, exp_data in data['experiments'].items():
        for response in exp_data['responses']:
            model_name = response['model'].lower()
            
            # Classify by family
            if 'claude' in model_name:
                family = 'claude'
            elif 'gpt' in model_name or 'chatgpt' in model_name:
                family = 'gpt'
            elif 'gemini' in model_name:
                family = 'gemini'
            elif 'llama' in model_name:
                family = 'llama'
            elif 'qwen' in model_name:
                family = 'qwen'
            else:
                family = 'other'
            
            model_families[family].append({
                'experiment': exp_name,
                'model': response['model'],
                'response': response['response']
            })
    
    return model_families

def create_convergence_visualization(df):
    """Create visualization of convergence patterns."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Convergence rates bar chart
    bars1 = ax1.bar(df['experiment'], df['convergence_rate'], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    ax1.set_title('Convergence Rates by Experiment', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Convergence Rate (%)')
    ax1.set_ylim(0, 60)
    
    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # Diversity index comparison
    bars2 = ax2.bar(df['experiment'], df['diversity_index'], color=['#96CEB4', '#FFEAA7', '#DDA0DD'])
    ax2.set_title('Diversity Index by Experiment', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Diversity Index (%)')
    ax2.set_ylim(0, 50)
    
    # Add value labels
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('plots/convergence_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_response_distribution_plots(data):
    """Create distribution plots for each experiment."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Response Distributions Across Experiments', fontsize=16, fontweight='bold')
    
    # Random Words
    word_data = data['experiments']['random_word_generation']
    word_counts = Counter()
    for response in word_data['responses']:
        word_counts[response['response']] += 1
    
    top_words = dict(word_counts.most_common(8))
    ax = axes[0, 0]
    bars = ax.bar(range(len(top_words)), list(top_words.values()), color='skyblue')
    ax.set_title('Random Word Generation', fontweight='bold')
    ax.set_xticks(range(len(top_words)))
    ax.set_xticklabels(list(top_words.keys()), rotation=45, ha='right')
    ax.set_ylabel('Number of Models')
    
    # Add value labels
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                str(int(height)), ha='center', va='bottom')
    
    # Jokes
    joke_data = data['experiments']['joke_generation']['analysis']['joke_categories']
    joke_names = [cat['category'] for cat in joke_data]
    joke_counts = [cat['count'] for cat in joke_data]
    
    ax = axes[0, 1]
    bars = ax.bar(range(len(joke_names)), joke_counts, color='lightcoral')
    ax.set_title('Joke Generation', fontweight='bold')
    ax.set_xticks(range(len(joke_names)))
    ax.set_xticklabels(joke_names, rotation=45, ha='right')
    ax.set_ylabel('Number of Models')
    
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                str(int(height)), ha='center', va='bottom')
    
    # Colors
    color_data = data['experiments']['color_selection']['analysis']['color_distribution']
    color_names = [color['color'] for color in color_data]
    color_counts = [color['count'] for color in color_data]
    
    ax = axes[1, 0]
    bars = ax.bar(range(len(color_names)), color_counts, color='lightgreen')
    ax.set_title('Color Selection', fontweight='bold')
    ax.set_xticks(range(len(color_names)))
    ax.set_xticklabels(color_names, rotation=45, ha='right')
    ax.set_ylabel('Number of Models')
    
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                str(int(height)), ha='center', va='bottom')
    
    # Temperature Analysis for Colors
    temp_data = data['experiments']['color_selection']['analysis']['color_temperature_analysis']
    temp_categories = ['Cool Colors', 'Warm Colors', 'Neutral Colors']
    temp_counts = [temp_data['cool_colors']['count'], 
                   temp_data['warm_colors']['count'], 
                   temp_data['neutral_colors']['count']]
    
    ax = axes[1, 1]
    colors_pie = ['lightblue', 'orange', 'lightgray']
    wedges, texts, autotexts = ax.pie(temp_counts, labels=temp_categories, autopct='%1.1f%%', 
                                     colors=colors_pie, startangle=90)
    ax.set_title('Color Temperature Distribution', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('plots/response_distributions.png', dpi=300, bbox_inches='tight')
    plt.show()

def calculate_statistical_metrics(data):
    """Calculate advanced statistical metrics."""
    results = {}
    
    for exp_name, exp_data in data['experiments'].items():
        responses = [r['response'] for r in exp_data['responses']]
        response_counts = Counter(responses)
        
        # Basic stats
        total_models = len(responses)
        unique_responses = len(response_counts)
        most_common = response_counts.most_common(1)[0]
        
        # Calculate Gini coefficient (inequality measure)
        counts = list(response_counts.values())
        counts.sort()
        n = len(counts)
        cumsum = np.cumsum(counts)
        gini = (2 * np.sum((np.arange(1, n+1) * counts))) / (n * cumsum[-1]) - (n+1)/n
        
        # Calculate entropy (diversity measure)
        probs = np.array(counts) / sum(counts)
        entropy = -np.sum(probs * np.log2(probs))
        max_entropy = np.log2(unique_responses)
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0
        
        results[exp_name] = {
            'total_models': total_models,
            'unique_responses': unique_responses,
            'most_common_response': most_common[0],
            'most_common_count': most_common[1],
            'convergence_rate': (most_common[1] / total_models) * 100,
            'diversity_index': (unique_responses / total_models) * 100,
            'gini_coefficient': gini,
            'entropy': entropy,
            'normalized_entropy': normalized_entropy
        }
    
    return results

def generate_report(data):
    """Generate comprehensive analysis report."""
    print("=" * 80)
    print("AI MODEL CONVERGENCE RESEARCH - COMPREHENSIVE ANALYSIS")
    print("=" * 80)
    
    # Statistical metrics
    stats = calculate_statistical_metrics(data)
    
    print("\nSTATISTICAL METRICS:")
    print("-" * 50)
    
    df_stats = pd.DataFrame(stats).T
    df_stats_display = df_stats[['total_models', 'unique_responses', 'convergence_rate', 
                                'diversity_index', 'gini_coefficient', 'normalized_entropy']]
    df_stats_display.columns = ['Models', 'Unique', 'Convergence%', 'Diversity%', 'Gini', 'Entropy']
    
    print(df_stats_display.round(2).to_string())
    
    # Model family analysis
    print(f"\n\nMODEL FAMILY ANALYSIS:")
    print("-" * 50)
    
    families = analyze_model_families(data)
    for family, responses in families.items():
        if responses:
            print(f"\n{family.upper()} models: {len(responses)} responses")
            
            # Count responses by experiment
            exp_counts = Counter(r['experiment'] for r in responses)
            for exp, count in exp_counts.items():
                print(f"  - {exp}: {count} models")
    
    # Convergence insights
    print(f"\n\nKEY INSIGHTS:")
    print("-" * 50)
    
    # Rank experiments by convergence
    convergence_ranking = sorted(stats.items(), key=lambda x: x[1]['convergence_rate'], reverse=True)
    
    print("Convergence Ranking (highest to lowest):")
    for i, (exp, data_exp) in enumerate(convergence_ranking, 1):
        print(f"{i}. {exp.replace('_', ' ').title()}: {data_exp['convergence_rate']:.1f}% on '{data_exp['most_common_response']}'")
    
    print(f"\nDiversity Ranking (most to least diverse):")
    diversity_ranking = sorted(stats.items(), key=lambda x: x[1]['diversity_index'], reverse=True)
    for i, (exp, data_exp) in enumerate(diversity_ranking, 1):
        print(f"{i}. {exp.replace('_', ' ').title()}: {data_exp['diversity_index']:.1f}% diversity index")
    
    return stats

def main():
    """Main analysis function."""
    # Create output directory
    Path("plots").mkdir(exist_ok=True)
    
    # Load data
    print("Loading research data...")
    data = load_data()
    
    # Generate comprehensive report
    stats = generate_report(data)
    
    # Create visualizations
    print(f"\nGenerating visualizations...")
    
    # Convergence analysis
    df = analyze_convergence_patterns(data)
    create_convergence_visualization(df)
    
    # Response distributions
    create_response_distribution_plots(data)
    
    print(f"\nAnalysis complete!")
    print(f"Plots saved in 'plots/' directory")
    print(f"- convergence_analysis.png: Convergence rates and diversity indices")
    print(f"- response_distributions.png: Response distributions for each experiment")

if __name__ == "__main__":
    main()
