#!/usr/bin/env python3
"""
Complete translation script for Clean Architecture book.
This script handles comprehensive Russian to English translation while preserving HTML structure.
"""

import os
import re
from pathlib import Path
from typing import Dict, Tuple

# Comprehensive translation dictionary
TRANSLATIONS: Dict[str, str] = {
    # Titles and headers
    "Введение - Clean Architecture Guide": "Introduction - Clean Architecture Guide",
    "SOLID в Python - Clean Architecture Guide": "SOLID in Python - Clean Architecture Guide",
    "Структура проекта - Clean Architecture Guide": "Project Structure - Clean Architecture Guide",
    "Dependency Injection - Clean Architecture Guide": "Dependency Injection - Clean Architecture Guide",
    "Domain Layer - Clean Architecture Guide": "Domain Layer - Clean Architecture Guide",
    "Application Layer - Clean Architecture Guide": "Application Layer - Clean Architecture Guide",
    "Infrastructure Layer - Clean Architecture Guide": "Infrastructure Layer - Clean Architecture Guide",
    "Presentation Layer - Clean Architecture Guide": "Presentation Layer - Clean Architecture Guide",
    "Middleware - Clean Architecture Guide": "Middleware - Clean Architecture Guide",
    "Aggregates - Clean Architecture Guide": "Aggregates - Clean Architecture Guide",
    "Инварианты - Clean Architecture Guide": "Invariants - Clean Architecture Guide",
    "Repository & UoW - Clean Architecture Guide": "Repository & UoW - Clean Architecture Guide",
    "Specification - Clean Architecture Guide": "Specification - Clean Architecture Guide",
    "Domain Events - Clean Architecture Guide": "Domain Events - Clean Architecture Guide",
    "Policies - Clean Architecture Guide": "Policies - Clean Architecture Guide",
    "Versioning - Clean Architecture Guide": "Versioning - Clean Architecture Guide",
    "Bounded Contexts - Clean Architecture Guide": "Bounded Contexts - Clean Architecture Guide",
    "Ubiquitous Language - Clean Architecture Guide": "Ubiquitous Language - Clean Architecture Guide",
    "Context Relationships - Clean Architecture Guide": "Context Relationships - Clean Architecture Guide",
    "ACL - Clean Architecture Guide": "ACL - Clean Architecture Guide",
    "Subdomains - Clean Architecture Guide": "Subdomains - Clean Architecture Guide",
    "Modular Monolith - Clean Architecture Guide": "Modular Monolith - Clean Architecture Guide",
    "Strategic Integration - Clean Architecture Guide": "Strategic Integration - Clean Architecture Guide",
    "Big Ball of Mud - Clean Architecture Guide": "Big Ball of Mud - Clean Architecture Guide",
    "Boundaries First - Clean Architecture Guide": "Boundaries First - Clean Architecture Guide",
    "CQRS и ES - Clean Architecture Guide": "CQRS & ES - Clean Architecture Guide",
    "Saga Pattern - Clean Architecture Guide": "Saga Pattern - Clean Architecture Guide",
    "Outbox Pattern - Clean Architecture Guide": "Outbox Pattern - Clean Architecture Guide",
    "Background Tasks - Clean Architecture Guide": "Background Tasks - Clean Architecture Guide",
    "Observability - Clean Architecture Guide": "Observability - Clean Architecture Guide",
    "Security - Clean Architecture Guide": "Security - Clean Architecture Guide",
    "Error Handling - Clean Architecture Guide": "Error Handling - Clean Architecture Guide",
    "Concurrency & Migrations - Clean Architecture Guide": "Concurrency & Migrations - Clean Architecture Guide",
    "Config & Logging - Clean Architecture Guide": "Config & Logging - Clean Architecture Guide",
    "Testing - Clean Architecture Guide": "Testing - Clean Architecture Guide",
    "Overengineering - Clean Architecture Guide": "Overengineering - Clean Architecture Guide",
    "Deployment - Clean Architecture Guide": "Deployment - Clean Architecture Guide",
    "Frameworks - Clean Architecture Guide": "Frameworks - Clean Architecture Guide",
    "Projects - Clean Architecture Guide": "Projects - Clean Architecture Guide",
    "Antipatterns - Clean Architecture Guide": "Antipatterns - Clean Architecture Guide",
    "Advanced Techniques - Clean Architecture Guide": "Advanced Techniques - Clean Architecture Guide",
    "Afterword - Clean Architecture Guide": "Afterword - Clean Architecture Guide",
    "Event Storming - Clean Architecture Guide": "Event Storming - Clean Architecture Guide",
    "Strategic Distillation - Clean Architecture Guide": "Strategic Distillation - Clean Architecture Guide",
    "Context Map - Clean Architecture Guide": "Context Map - Clean Architecture Guide",
    
    # Navigation sections
    "Основы": "Fundamentals",
    "Слои архитектуры": "Architecture Layers", 
    "Тактический DDD": "Tactical DDD",
    "Стратегический DDD": "Strategic DDD",
    "CQRS и Распределенные системы": "CQRS & Distributed Systems",
    "Надежность и Безопасность": "Reliability & Security",
    "Качество и Практика": "Quality & Practice",
    "О проекте": "About",
    
    # Navigation items  
    "Введение": "Introduction",
    "SOLID принципы": "SOLID Principles",
    "Структура проекта (DDD)": "Project Structure (DDD)",
    "Инварианты": "Invariants",
    "Тестирование": "Testing",
    "Избыточность": "Overengineering",
    "Мини-проекты": "Mini-projects",
    "Антипаттерны": "Antipatterns",
    "Послесловие": "Afterword",
    
    # Navigation/UI elements
    "Далее": "Next",
    "Назад": "Previous",
    "Предыдущая": "Previous",
    "Следующая": "Next",
    
    # Common phrases (will be done file by file with more detail)
}

def update_language_attributes(content: str) -> str:
    """Update HTML language attributes and language switcher."""
    # Change lang attribute
    content = content.replace('lang="ru"', 'lang="en"')
    
    # Update language switcher for all files - make EN active
    # Match patterns like: <a href="index.html" class="text-blue-400 font-bold">RU</a>
    # or <a href="solid.html" class="text-blue-400 font-bold">RU</a>
    content = re.sub(
        r'<a href="([^"]+\.html)" class="text-blue-400 font-bold">RU</a>',
        r'<a href="../ru/\1" class="hover:text-white transition">RU</a>',
        content
    )
    
    # Update EN link to be active
    content = re.sub(
        r'<a href="\.\./en/([^"]+\.html)" class="hover:text-white transition">EN</a>',
        r'<a href="\1" class="text-blue-400 font-bold">EN</a>',
        content
    )
    
    return content

def apply_translations(content: str) -> str:
    """Apply translation dictionary to content."""
    for ru, en in TRANSLATIONS.items():
        # Translate in titles
        content = content.replace(f'<title>{ru}</title>', f'<title>{en}</title>')
        # Translate in navigation and content
        content = content.replace(f'>{ru}<', f'>{en}<')
        content = content.replace(f'"{ru}"', f'"{en}"')
    
    return content

def translate_html_file(input_path: Path, output_path: Path):
    """Translate a single HTML file."""
    print(f"Processing: {input_path.name}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply basic transformations
    content = update_language_attributes(content)
    content = apply_translations(content)
    
    # Write output
    os.makedirs(output_path.parent, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Main function."""
    ru_dir = Path("/home/runner/work/books.github.io/books.github.io/book_clean_architecture/ru")
    en_dir = Path("/home/runner/work/books.github.io/books.github.io/book_clean_architecture/en")
    
    en_dir.mkdir(exist_ok=True)
    
    html_files = sorted(ru_dir.glob("*.html"))
    
    print(f"Translating {len(html_files)} HTML files...")
    print("=" * 60)
    
    for html_file in html_files:
        output_file = en_dir / html_file.name
        translate_html_file(html_file, output_file)
    
    print("=" * 60)
    print(f"✓ Basic translation complete for {len(html_files)} files")
    print(f"✓ Files created in: {en_dir}")
    print("\nNote: This handles structure and navigation.")
    print("Full content translation will be done file-by-file with detailed content.")

if __name__ == "__main__":
    main()
