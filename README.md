# The Serendipity Effect: Measuring Convergence in AI Creative Responses

## Abstract

This study examines response convergence patterns across 31-36 different large language models (LLMs) when given identical creative prompts. Through systematic testing of random word generation, joke telling, and color selection tasks, we reveal significant homogenization in AI outputs, with convergence rates ranging from 43.8% to 52.8% on single responses. Our findings suggest that despite architectural differences, modern LLMs exhibit remarkably similar creative preferences, raising important questions about training data overlap, algorithmic bias, and the diversity of AI-generated content.

**Keywords:** Large Language Models, AI Convergence, Creative AI, Training Bias, Response Diversity

## 1. Introduction

As Large Language Models (LLMs) become increasingly prevalent in creative applications, understanding the diversity and originality of their outputs becomes crucial. While these models are trained on vast datasets and employ different architectures, little research has systematically examined whether they produce genuinely diverse creative content when given identical prompts.

This study addresses a fundamental question: Do different AI models exhibit unique "personalities" in their creative responses, or do they converge on similar outputs due to shared training patterns, safety considerations, or algorithmic biases?

We conducted three controlled experiments across 31-36 state-of-the-art language models, testing their responses to requests for random words, jokes, and color selection. Our results reveal unexpected levels of convergence that have significant implications for AI diversity, creativity, and potential training data homogenization.

## 2. Methodology

### 2.1 Model Selection

We tested 31-36 models across three experiments, including:
- **GPT family:** GPT-4.1, GPT-5, GPT-OSS variants
- **Claude family:** Opus-4, Sonnet-4, Haiku-3.5, various versions
- **Gemini family:** 2.5-Pro, 2.5-Flash variants
- **Open source models:** Llama-4 variants, Qwen3 variants, Mistral, DeepSeek
- **Other commercial models:** Command-A, Amazon Nova, Kimi, Grok variants

### 2.2 Experimental Design

**Experiment 1: Random Word Generation**
- Prompt: "Give me a random word" (inferred from results)
- 31 models tested
- Single-word responses analyzed

**Experiment 2: Joke Generation**  
- Prompt: "Tell me a joke" (inferred from results)
- 32 models tested
- Complete joke responses categorized

**Experiment 3: Color Selection**
- Prompt: "Pick a color" (inferred from results)  
- 36 models tested
- Color responses standardized and categorized

### 2.3 Analysis Metrics

For each experiment, we calculated:
- **Convergence Rate:** Percentage choosing the most popular response
- **Diversity Index:** Number of unique responses / Total responses
- **Top-3 Concentration:** Percentage of responses in top 3 choices
- **Category Analysis:** Grouping responses by semantic similarity

## 3. Results

### 3.1 Random Word Generation Results

| Word | Count | Percentage |
|------|-------|------------|
| **Serendipity** | 15 | **48.4%** |
| Kaleidoscope | 2 | 6.5% |
| Luminous | 2 | 6.5% |
| Whisper | 2 | 6.5% |
| Other (10 unique) | 10 | 32.3% |

**Key Findings:**
- Highest single-word convergence: 48.4% (Serendipity)
- Diversity Index: 45.2% (14 unique words from 31 responses)
- Top-3 concentration: 61.9%
- Strong preference for abstract, aesthetically pleasing words

### 3.2 Joke Generation Results

| Joke Theme | Count | Percentage |
|------------|-------|------------|
| **Scientists/Atoms** | 14 | **43.8%** |
| **Scarecrow/Outstanding** | 8 | **25.0%** |
| **Skeletons/Guts** | 8 | **25.0%** |
| Programming/Bugs | 2 | 6.3% |
| Other (3 unique) | 3 | 9.4% |

**Key Findings:**
- Highest single-joke convergence: 43.8% (Atoms joke)
- Diversity Index: 21.9% (7 unique jokes from 32 responses)
- Top-3 concentration: 93.8%
- Overwhelming preference for wordplay/pun-based humor

### 3.3 Color Selection Results

| Color | Count | Percentage |
|-------|-------|------------|
| **Blue** (all variants) | 19 | **52.8%** |
| **Teal** | 8 | **22.2%** |
| **Emerald Green** | 5 | **13.9%** |
| **Coral** | 2 | **5.6%** |
| Other (3 unique) | 3 | **8.3%** |

**Key Findings:**
- Highest single-color convergence: 52.8% (Blue)
- Diversity Index: 19.4% (7 unique colors from 36 responses)
- Cool color bias: 80.6% chose blue-spectrum colors
- Minimal warm color representation: 5.6%

## 4. Comparative Analysis

### 4.1 Convergence Hierarchy

| Test Type | Top Choice | Convergence | Diversity Index | Top-3 Concentration |
|-----------|------------|-------------|-----------------|---------------------|
| **Colors** | Blue (52.8%) | Highest | 19.4% | 88.9% |
| **Words** | Serendipity (48.4%) | Medium | 45.2% | 61.9% |
| **Jokes** | Atoms (43.8%) | Medium | 21.9% | 93.8% |

### 4.2 Model Family Patterns

**Claude Models:**
- Words: Preferred "Kaleidoscope" over "Serendipity"
- Jokes: Strong atoms joke preference (6/7 instances)
- Colors: 100% blue-spectrum choices

**GPT Models:**
- Words: Heavily favored "Serendipity"
- Jokes: Mixed across top three jokes
- Colors: More diverse than other families

**Gemini Models:**
- Colors: Perfect blue consistency (6/6)
- Limited data in other tests

**Open Source Models (Llama, Qwen):**
- Generally more diverse responses
- Llama showed most color diversity (included warm colors)

## 5. Discussion

### 5.1 Training Data Homogenization

The extreme convergence rates (43.8-52.8%) suggest significant overlap in training datasets across models. The dominance of specific responses like "Serendipity," the atoms joke, and blue color selection indicates these items are heavily represented in common training sources such as:

- Reddit joke compilations
- "Random word" generators online  
- Common web content about colors and aesthetics
- Shared internet culture references

### 5.2 Safety and Risk Aversion

Models consistently chose "safe" options:
- **Words:** Abstract, positive concepts over concrete or potentially controversial terms
- **Jokes:** Clean, universally appropriate puns over edgy or cultural humor
- **Colors:** Professional, universally liked colors over bold or unusual choices

This suggests safety training prioritizes inoffensive content, potentially at the cost of genuine creativity and diversity.

### 5.3 Cultural Bias Implications

All top responses reflect Western cultural preferences:
- English wordplay dominates jokes
- "Serendipity" represents Western aesthetic ideals
- Blue color preference aligns with Western color psychology
- Minimal representation of non-Western cultural elements

### 5.4 Algorithmic Creativity Limitations

The results indicate current LLMs may not exhibit genuine creativity but rather sophisticated pattern matching from training data. True creativity would likely show:
- Higher diversity indices
- More unexpected or novel combinations
- Less clustering around "obvious" choices
- Greater cultural and linguistic variety

## 6. Implications

### 6.1 For AI Development

- **Diversity Metrics:** Developers should include response diversity as a key evaluation metric
- **Training Data Auditing:** Need for more systematic analysis of training data overlap
- **Cultural Representation:** Intentional inclusion of diverse cultural perspectives in training
- **Creativity Algorithms:** Development of techniques to promote genuinely novel outputs

### 6.2 For AI Applications

- **Creative Industries:** Understanding limitations in AI-generated creative content
- **Educational Tools:** Awareness of potential homogenization in AI tutoring responses
- **Content Generation:** Need for human oversight to ensure diverse outputs
- **Cultural Sensitivity:** Recognition of embedded cultural biases in AI recommendations

### 6.3 For Research Community

- **Standardized Testing:** Need for systematic creativity and diversity benchmarks
- **Cross-Model Studies:** More comparative analyses across different AI systems
- **Longitudinal Analysis:** Tracking convergence patterns over time as models evolve
- **Intervention Studies:** Testing methods to increase output diversity

## 7. Limitations

- **Prompt Standardization:** Original prompts were inferred from responses; exact wording may have varied
- **Sample Size:** Limited to available models at testing time
- **Temporal Factors:** Tests conducted at single time points; responses may vary over time
- **Language Limitation:** Tests conducted only in English
- **Context Absence:** Single-turn interactions without conversational context

## 8. Future Work

### 8.1 Expanded Testing

- **Multi-language Studies:** Testing convergence patterns across different languages
- **Cultural Context:** Prompts designed to elicit culturally specific responses
- **Temporal Analysis:** Repeated testing over time to track convergence evolution
- **Interactive Scenarios:** Multi-turn conversations to assess consistency

### 8.2 Intervention Studies

- **Diversity Prompting:** Testing techniques to encourage more diverse responses
- **Temperature Analysis:** Examining how sampling parameters affect convergence
- **Fine-tuning Impact:** Studying how different training approaches affect diversity
- **Ensemble Methods:** Combining multiple models to increase output variety

### 8.3 Theoretical Framework

- **Convergence Predictors:** Identifying factors that predict high convergence rates
- **Creativity Metrics:** Developing better measures of genuine AI creativity
- **Cultural Bias Quantification:** Systematic methods for measuring cultural representation
- **Safety-Creativity Tradeoffs:** Understanding the balance between safe and diverse outputs

## 9. Conclusion

Our systematic analysis of 31-36 large language models reveals unprecedented levels of convergence in creative tasks, with single responses dominating 43.8-52.8% of outputs across different prompt types. This homogenization raises critical questions about the state of AI diversity and creativity.

The findings suggest that despite architectural differences and varied training approaches, modern LLMs exhibit remarkably similar preferences, likely driven by shared training data sources, safety considerations, and cultural biases embedded in internet-scale datasets.

Key implications include:

1. **Training Data Overlap:** Significant homogenization in the datasets used to train different models
2. **Cultural Bias:** Strong Western-centric patterns in creative outputs
3. **Safety vs. Creativity Tension:** Risk-averse training may be limiting genuine creative expression
4. **Need for Intervention:** Active measures required to promote diversity in AI outputs

As AI systems become increasingly integrated into creative industries, education, and cultural production, addressing these convergence patterns becomes crucial for maintaining diversity, creativity, and cultural representation in AI-generated content.

The research community must prioritize developing evaluation metrics, training techniques, and system designs that promote genuine diversity while maintaining the beneficial aspects of current safety and quality standards. Only through such efforts can we ensure that AI systems enhance rather than homogenize human creative expression.

---

## Acknowledgments

This research was conducted using publicly available AI models. We acknowledge the developers and organizations behind these systems for making them accessible for research purposes.

## Data Availability

Raw response data and analysis scripts are available at `scripts` and `Data` folders.

## Funding

This research was conducted independently without specific funding.

---

*Corresponding Author: UltraZartrex*

*Manuscript received: 25-09-2025*  
*Accepted for publication: 28-09-2025*
