#!/usr/bin/env python3
"""
Simple Model Handler
Handles Ollama model interactions
"""

import logging
from openai import OpenAI
from typing import Optional

logger = logging.getLogger(__name__)

class ModelHandler:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize Ollama client"""
        try:
            self.client = OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama"
            )
            logger.info(f"✅ Ollama client initialized for model: {self.model_name}")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Ollama client: {e}")
            self.client = None
    
    def test_connection(self) -> bool:
        """Test if the model is available"""
        if not self.client:
            return False
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5,
                timeout=10
            )
            logger.info(f"✅ Model {self.model_name} is available")
            return True
        except Exception as e:
            logger.error(f"❌ Model {self.model_name} not available: {e}")
            return False
    
    def generate_content(self, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> Optional[str]:
        """Generate content using the model"""
        if not self.client:
            raise Exception("Ollama client not initialized")
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                max_tokens=3000,
                stream=False
            )
            
            content = response.choices[0].message.content.strip()
            logger.info(f"✅ Content generated successfully ({len(content)} characters)")
            return content
            
        except Exception as e:
            logger.error(f"❌ Content generation failed: {e}")
            return None
