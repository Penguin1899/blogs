#!/usr/bin/env python3
"""
Simple Topic Selector
Randomly picks a topic from predefined topics
"""

import random
from typing import Dict, List

class TopicSelector:
    def __init__(self):
        self.topics = [
            {
                'title': 'Modern DevOps Practices',
                'category': 'tech',
                'keywords': ['DevOps', 'CI/CD', 'automation', 'infrastructure'],
                'description': 'Exploring cutting-edge DevOps methodologies and automation tools'
            },
            {
                'title': 'Kubernetes Best Practices',
                'category': 'tech', 
                'keywords': ['Kubernetes', 'containers', 'orchestration', 'deployment'],
                'description': 'Production-ready Kubernetes deployment strategies and best practices'
            },
            {
                'title': 'Infrastructure as Code',
                'category': 'tech',
                'keywords': ['Terraform', 'IaC', 'automation', 'cloud'],
                'description': 'Managing infrastructure through declarative code'
            },
            {
                'title': 'Site Reliability Engineering',
                'category': 'tech',
                'keywords': ['SRE', 'monitoring', 'reliability', 'observability'],
                'description': 'Building and maintaining reliable systems at scale'
            },
            {
                'title': 'Docker Security Practices',
                'category': 'tutorials',
                'keywords': ['Docker', 'security', 'containers', 'hardening'],
                'description': 'Securing containerized applications and infrastructure'
            },
            {
                'title': 'GitOps Workflows',
                'category': 'tutorials',
                'keywords': ['GitOps', 'Git', 'deployment', 'automation'],
                'description': 'Implementing GitOps for reliable deployments'
            },
            {
                'title': 'Cloud Migration Strategies',
                'category': 'tutorials',
                'keywords': ['cloud', 'migration', 'AWS', 'strategy'],
                'description': 'Planning and executing successful cloud migrations'
            },
            {
                'title': 'Platform Engineering Insights',
                'category': 'personal',
                'keywords': ['platform', 'developer experience', 'productivity'],
                'description': 'Building platforms that empower development teams'
            },
            {
                'title': 'DevOps Career Journey',
                'category': 'personal',
                'keywords': ['career', 'growth', 'skills', 'leadership'],
                'description': 'Lessons learned from a DevOps engineering career'
            },
            {
                'title': 'Building Engineering Culture',
                'category': 'personal',
                'keywords': ['culture', 'team', 'collaboration', 'leadership'],
                'description': 'Creating a positive engineering culture and team dynamics'
            }
        ]
    
    def get_random_topic(self) -> Dict:
        """Get a random topic"""
        return random.choice(self.topics)
    
    def get_all_topics(self) -> List[Dict]:
        """Get all available topics"""
        return self.topics
