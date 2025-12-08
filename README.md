# AI-Powered Tech Blog

This repository contains an AI-powered blog built with Hugo that automatically generates and publishes technical content twice weekly using GitHub Actions.

## 🏗️ Architecture

```
blogs/
├── .github/
│   └── workflows/
│       └── hugo-deploy.yml      # Automated deployment and AI content generation
├── content/
│   ├── posts/                   # Blog posts (markdown files)
│   └── search/                  # Search functionality  
├── scripts/
│   ├── ai_content_generator.py  # AI content generation script
│   └── topics.yaml             # Topic configuration and scheduling
├── themes/
│   └── PaperMod/               # Hugo theme (git submodule)
├── static/                     # Static assets
├── hugo.yaml                   # Hugo configuration
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

1. **Hugo** (Extended version)
2. **Git** with submodules support
3. **Python 3.11+** (for AI content generation)

### Installation

#### macOS (using Homebrew)
```bash
# Install Hugo
brew install hugo

# Clone the repository
git clone --recurse-submodules https://github.com/Penguin1899/blogs.git
cd blogs

# Install Python dependencies
pip install openai pyyaml requests beautifulsoup4 markdown
```

#### Linux (Ubuntu/Debian)
```bash
# Install Hugo
sudo snap install hugo

# Or download from GitHub releases
wget https://github.com/gohugoio/hugo/releases/download/v0.120.0/hugo_extended_0.120.0_linux-amd64.deb
sudo dpkg -i hugo_extended_0.120.0_linux-amd64.deb

# Clone the repository
git clone --recurse-submodules https://github.com/Penguin1899/blogs.git
cd blogs

# Install Python dependencies
pip install openai pyyaml requests beautifulsoup4 markdown
```

#### Windows
```bash
# Install Hugo using Chocolatey
choco install hugo-extended

# Or download from GitHub releases and add to PATH
# https://github.com/gohugoio/hugo/releases

# Clone the repository
git clone --recurse-submodules https://github.com/Penguin1899/blogs.git
cd blogs

# Install Python dependencies
pip install openai pyyaml requests beautifulsoup4 markdown
```

## 🛠️ Local Development

### Build and Serve Locally

```bash
# Navigate to blog directory
cd blogs/

# Start Hugo development server with local baseURL
hugo server --buildDrafts --baseURL http://localhost:1313

# Or with navigate to changed files (recommended for development)
hugo server --buildDrafts --baseURL http://localhost:1313 --navigateToChanged

# With custom port
hugo server --buildDrafts --baseURL http://localhost:1314 --port 1314
```

**📝 Important**: Always use the `--baseURL` flag for local development to override the production URL configured in `hugo.yaml`.

The blog will be available at: **http://localhost:1313** (or your custom port)

### Development Commands Quick Reference

```bash
# Basic development server
hugo server --buildDrafts --baseURL http://localhost:1313

# Full development setup (recommended)
hugo server --buildDrafts --navigateToChanged --baseURL http://localhost:1313

# Custom port (if 1313 is busy)
hugo server --buildDrafts --baseURL http://localhost:1314 --port 1314

# Open browser automatically
hugo server --buildDrafts --baseURL http://localhost:1313 --openBrowser

# Production build test
hugo --minify
```

### Create New Content

```bash
# Create a new blog post
hugo new content posts/my-new-post.md

# Edit the post
nano content/posts/my-new-post.md

# Set draft: false when ready to publish
```

### Build for Production

```bash
# Build static site
hugo --minify

# Output will be in ./public/ directory
```

## 🤖 AI Content Generation

### Manual AI Content Generation

```bash
# Generate AI content manually
python scripts/ai_content_generator.py
```

### Configure Topics

Edit `scripts/topics.yaml` to customize:

- **Topics**: Subject areas and keywords
- **Schedule**: Frequency and timing
- **Guidelines**: Content requirements and style

```yaml
topics:
  - category: "devops"
    title: "Modern DevOps Practices"
    keywords: ["CI/CD", "automation", "infrastructure"]
    difficulty: "intermediate"

schedule:
  frequency: "twice_weekly" 
  days: ["tuesday", "friday"]
  time: "10:00"
```

## 🚀 Automated Deployment

### GitHub Actions Workflow

The blog automatically:

1. **Builds and deploys** on every push to main/master
2. **Generates AI content** twice weekly (Tuesday & Friday at 10:00 UTC)
3. **Validates content** before publishing
4. **Commits generated posts** back to repository

### Workflow Triggers

- **Push to main**: Builds and deploys site
- **Pull requests**: Builds and validates (no deployment)  
- **Schedule**: Generates AI content (Tuesdays & Fridays)
- **Manual**: Workflow can be triggered manually

### Environment Variables

For AI content generation, set these GitHub repository secrets:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## 📁 Content Structure

### Blog Posts

All blog posts are stored in `content/posts/` as Markdown files with YAML frontmatter:

```yaml
---
title: "Post Title"
date: 2025-12-08T10:00:00Z
draft: false
tags: ["devops", "automation"]
categories: ["technology"]
description: "Post description for SEO"
cover:
    image: ""
    alt: "Alt text"
showToc: true
ai_generated: true  # For AI-generated posts
---

## Introduction

Your content here...
```

### Tags and Categories

- **Tags**: Specific keywords (`docker`, `kubernetes`, `ci-cd`)
- **Categories**: Broad areas (`devops`, `cloud`, `ai`, `tools`)

## 🎨 Customization

### Hugo Configuration

Edit `hugo.yaml` to customize:

- **Site settings**: Title, description, URLs
- **Theme parameters**: Colors, fonts, layout
- **Social links**: GitHub, LinkedIn, etc.
- **Analytics**: Google Analytics integration

### Theme Customization

The blog uses the [PaperMod theme](https://github.com/adityatelange/hugo-PaperMod). To customize:

1. **Override layouts**: Create files in `layouts/` directory
2. **Custom CSS**: Add styles in `assets/css/extended/`  
3. **Custom JavaScript**: Add scripts in `assets/js/`

## 🔧 Troubleshooting

### Common Issues

**Hugo not found**
```bash
# Verify Hugo installation
hugo version

# Should show: hugo v0.120.0+extended
```

**Theme not loading**
```bash
# Update git submodules
git submodule update --init --recursive

# Or re-clone with submodules
git clone --recurse-submodules <repository-url>
```

**AI content generation fails**
```bash
# Check Python dependencies
pip list | grep -E "(openai|yaml|requests)"

# Install missing dependencies
pip install -r requirements.txt
```

**Build errors**
```bash
# Check Hugo configuration
hugo config

# Validate content files
hugo --printI18nWarnings
```

## 📊 Performance

### Build Times

- **Local development**: ~50ms for incremental builds
- **Full production build**: ~200ms for entire site
- **GitHub Actions deployment**: ~2-3 minutes total

### Optimization

The blog is optimized for:

- **Fast loading**: Minified HTML, CSS, JS
- **SEO**: Proper meta tags and structured data  
- **Mobile**: Responsive design and fast rendering
- **Accessibility**: Semantic HTML and proper contrast

## 🤝 Contributing

### Adding Content

1. Fork the repository
2. Create a new branch: `git checkout -b feature/new-post`
3. Add your content: `hugo new content posts/your-post.md`
4. Submit a pull request

### Improving AI Generation

1. Update `scripts/topics.yaml` with new topics
2. Enhance `scripts/ai_content_generator.py` with better AI integration
3. Test locally before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Live Blog**: https://penguin1899.github.io/blogs
- **Hugo Documentation**: https://gohugo.io/documentation/
- **PaperMod Theme**: https://github.com/adityatelange/hugo-PaperMod
- **GitHub Actions**: https://docs.github.com/en/actions
