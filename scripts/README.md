# Simple AI Content Generator

A clean, modular AI content generator that randomly picks topics and creates blog posts using Ollama.

## Features

- 🎯 **Simple & Focused**: Only uses the model you specify via `--model`
- 📝 **Random Topic Selection**: Automatically picks from curated topics
- 📁 **Smart Organization**: Saves posts to correct category folders
- 🚀 **Fast Generation**: Direct integration with Ollama
- 🔧 **Modular Design**: Separate modules for different concerns

## Files

- `generate.py` - Main script
- `topic_selector.py` - Handles topic selection
- `model_handler.py` - Manages Ollama model interactions
- `content_generator.py` - Creates and saves blog posts

## Usage

### Prerequisites

1. Install Ollama: `brew install ollama`
2. Pull a model: `ollama pull llama3.2:latest`
3. Install OpenAI Python library: `pip install openai`

### Generate Content

```bash
# Generate a blog post using a specific model
python scripts/generate.py --model llama3.2:latest

# List available topics
python scripts/generate.py --model llama3.2:latest --list

# Enable verbose logging
python scripts/generate.py --model llama3.2:latest --verbose
```

## How It Works

1. **Topic Selection**: Randomly selects from predefined topics
2. **Model Connection**: Connects to specified Ollama model only
3. **Content Generation**: Creates comprehensive blog post content
4. **File Organization**: Saves to `content/{category}/` with proper frontmatter
5. **Fallback**: Creates template if AI generation fails

## Sample Output

```
🤖 Testing connection to model: llama3.2:latest
✅ Model llama3.2:latest is available
📝 Selected topic: Docker Security Practices (tutorials)
🚀 Generating content using llama3.2:latest...
✅ Content generated and saved!
📁 File: content/tutorials/2026-01-21-docker-security-practices.md
📊 Word count: 641 words
```

## Topics Available

- **Tech**: DevOps, Kubernetes, SRE, Infrastructure as Code
- **Tutorials**: Docker Security, GitOps, Cloud Migration
- **Personal**: Platform Engineering, Career Journey, Team Culture

## Configuration

Topics are hardcoded in `topic_selector.py` for simplicity. Edit this file to add/modify topics.

## No Complexity, Just Results

This system intentionally avoids:
- Complex model fallback logic
- Advanced topic scoring algorithms
- Extensive configuration files
- Multiple model management

It focuses on: **Pick a topic → Use your model → Generate content → Save it**
