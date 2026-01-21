#!/usr/bin/env python3
"""
Simple AI Content Generator
Randomly picks a topic and generates content using the specified model
"""

import argparse
import logging
import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from topic_selector import TopicSelector
from model_handler import ModelHandler
from content_generator import ContentGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Simple AI Content Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --model llama3.2:latest        # Generate content with specific model
  %(prog)s --model llama3:8b --list       # List available topics
        """
    )
    
    parser.add_argument(
        '--model', 
        required=True,
        help='Ollama model to use (e.g., llama3.2:latest, llama3:8b)'
    )
    parser.add_argument(
        '--list', 
        action='store_true',
        help='List all available topics'
    )
    parser.add_argument(
        '--verbose', '-v', 
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        # Initialize components
        topic_selector = TopicSelector()
        model_handler = ModelHandler(args.model)
        content_generator = ContentGenerator()
        
        # List topics if requested
        if args.list:
            print("📋 Available Topics:")
            print("=" * 50)
            for i, topic in enumerate(topic_selector.get_all_topics(), 1):
                print(f"{i:2d}. {topic['title']}")
                print(f"    Category: {topic['category']}")
                print(f"    Keywords: {', '.join(topic['keywords'])}")
                print(f"    Description: {topic['description']}")
                print()
            return 0
        
        # Test model connection
        print(f"🤖 Testing connection to model: {args.model}")
        if not model_handler.test_connection():
            print(f"❌ Model {args.model} is not available")
            print("Make sure Ollama is running and the model is installed")
            print(f"Try: ollama pull {args.model}")
            return 1
        
        # Select random topic
        topic = topic_selector.get_random_topic()
        print(f"📝 Selected topic: {topic['title']} ({topic['category']})")
        
        # Generate prompts
        system_prompt = content_generator.create_system_prompt()
        user_prompt = content_generator.create_user_prompt(topic)
        
        # Generate content
        print(f"🚀 Generating content using {args.model}...")
        content = model_handler.generate_content(system_prompt, user_prompt)
        
        if content:
            # Save post
            filepath = content_generator.save_post(topic, content)
            print(f"✅ Content generated and saved!")
            print(f"📁 File: {filepath}")
            print(f"📊 Word count: {len(content.split())} words")
        else:
            # Create fallback
            print("⚠️ AI generation failed, creating template...")
            filepath = content_generator.create_fallback_post(topic)
            print(f"📁 Template created: {filepath}")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n🛑 Cancelled by user")
        return 1
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit(main())
