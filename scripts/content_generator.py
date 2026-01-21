#!/usr/bin/env python3
"""
Simple Content Generator
Creates blog posts and saves them to the correct folders
"""

import os
import re
import datetime
from pathlib import Path
from typing import Dict

class ContentGenerator:
    def __init__(self, base_dir: str = "content"):
        self.base_dir = Path(base_dir)
        
    def create_system_prompt(self) -> str:
        """Create system prompt for AI"""
        return """You are an expert DevOps Engineer and Site Reliability Engineer with 15+ years of experience at leading tech companies. 

Write practical, actionable blog posts that include:
- Real-world examples and code snippets
- Specific tools and commands
- Best practices from production experience
- Common pitfalls and how to avoid them
- Step-by-step implementation guides

Your writing style:
- Conversational but authoritative
- Include specific examples with actual code
- Share both successes and failures
- Focus on practical value
- Use clear headings and structure"""
    
    def create_user_prompt(self, topic: Dict) -> str:
        """Create user prompt for specific topic"""
        return f"""Write a comprehensive blog post about "{topic['title']}".

Topic details:
- Category: {topic['category']}
- Keywords: {', '.join(topic['keywords'])}
- Description: {topic['description']}

Requirements:
1. 1500-2500 words of practical content
2. Include 3-5 code examples or configurations
3. Structure with clear H2/H3 headers
4. Share real-world scenarios and lessons learned
5. Include troubleshooting tips and best practices
6. End with actionable next steps

Write ONLY the markdown content (no YAML frontmatter). Start with an engaging introduction."""
    
    def create_frontmatter(self, topic: Dict, content: str) -> str:
        """Create YAML frontmatter for the post"""
        title = topic['title']
        date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
        if not date.endswith(('+', '-')):
            date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+05:30')
        
        # Calculate reading time (200 words per minute)
        word_count = len(content.split())
        reading_time = max(1, round(word_count / 200))
        
        return f"""---
title: "{title}"
date: {date}
draft: false
tags: {topic['keywords']}
categories: ["{topic['category']}"]
description: "{topic['description']}"
showToc: true
TocOpen: false
word_count: {word_count}
reading_time: {reading_time}
author: "DevOps Expert"
---

"""
    
    def generate_filename(self, title: str) -> str:
        """Generate URL-friendly filename"""
        # Clean title
        clean_title = re.sub(r'[^\w\s-]', '', title.lower())
        slug = re.sub(r'[-\s]+', '-', clean_title)
        
        # Add date
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        
        return f"{today}-{slug}.md"
    
    def save_post(self, topic: Dict, content: str) -> str:
        """Save the generated post to correct folder"""
        # Create category directory
        category_dir = self.base_dir / topic['category']
        category_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename
        filename = self.generate_filename(topic['title'])
        filepath = category_dir / filename
        
        # Check if file already exists
        if filepath.exists():
            # Add timestamp to make unique
            timestamp = datetime.datetime.now().strftime('%H%M%S')
            base_name = filepath.stem
            new_filename = f"{base_name}-{timestamp}.md"
            filepath = category_dir / new_filename
        
        # Create full content with frontmatter
        frontmatter = self.create_frontmatter(topic, content)
        full_content = frontmatter + content
        
        # Add footer
        footer = f"""

---

*This article was generated using AI with technical validation. Have questions or feedback? Feel free to reach out!*
"""
        full_content += footer
        
        # Save file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        return str(filepath)
    
    def create_fallback_post(self, topic: Dict) -> str:
        """Create a template post when AI generation fails"""
        template_content = f"""# {topic['title']}

## Introduction

{topic['description']}

## Key Concepts

[Content to be added]

## Implementation

[Implementation steps needed]

## Best Practices

[Best practices to be documented]

## Conclusion

[Summary and next steps]

---

**Note**: This is a template post created when AI generation was unavailable. Manual completion required."""
        
        return self.save_post(topic, template_content)
