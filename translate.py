#!/usr/bin/env python3
"""
Translation script for Clean Architecture book from Russian to English.
Translates all HTML files while preserving structure and code.
"""

import os
import re
from pathlib import Path

# Translation dictionary for common terms and navigation
TRANSLATIONS = {
    # Page sections
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
    "Domain Layer": "Domain Layer",
    "Application Layer": "Application Layer",
    "Infrastructure Layer": "Infrastructure Layer",
    "Presentation Layer": "Presentation Layer",
    "Middleware": "Middleware",
    "Aggregates": "Aggregates",
    "Инварианты": "Invariants",
    "Repository & UoW": "Repository & UoW",
    "Specification": "Specification",
    "Domain Events": "Domain Events",
    "Policies": "Policies",
    "Versioning": "Versioning",
    "Bounded Contexts": "Bounded Contexts",
    "Ubiquitous Language": "Ubiquitous Language",
    "Context Relationships": "Context Relationships",
    "Anti-Corruption Layer": "Anti-Corruption Layer",
    "Subdomains": "Subdomains",
    "Modular Monolith": "Modular Monolith",
    "Strategic Integration": "Strategic Integration",
    "Big Ball of Mud": "Big Ball of Mud",
    "Boundaries First": "Boundaries First",
    "CQRS и ES": "CQRS & ES",
    "Saga Pattern": "Saga Pattern",
    "Outbox Pattern": "Outbox Pattern",
    "Background Tasks": "Background Tasks",
    "Observability": "Observability",
    "Auth & Permissions": "Auth & Permissions",
    "Error Handling": "Error Handling",
    "Concurrency & Migrations": "Concurrency & Migrations",
    "Config & Observability": "Config & Observability",
    "Тестирование": "Testing",
    "Избыточность": "Overengineering",
    "Deployment & Protection": "Deployment & Protection",
    "Django & Others": "Django & Others",
    "Мини-проекты": "Mini-projects",
    "Антипаттерны": "Antipatterns",
    "Advanced Tech": "Advanced Tech",
    "Послесловие": "Afterword",
    
    # Common UI elements
    "Далее": "Next",
    "Назад": "Previous",
    "Предыдущая": "Previous",
    "Следующая": "Next",
}

def translate_file(input_path: Path, output_path: Path):
    """Translate a single HTML file from Russian to English."""
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change lang attribute
    content = content.replace('lang="ru"', 'lang="en"')
    
    # Update language switcher links - RU should not be active
    content = re.sub(
        r'<a href="index\.html" class="text-blue-400 font-bold">RU</a>',
        r'<a href="../ru/index.html" class="hover:text-white transition">RU</a>',
        content
    )
    content = re.sub(
        r'<a href="\.\./en/index\.html" class="hover:text-white transition">EN</a>',
        r'<a href="index.html" class="text-blue-400 font-bold">EN</a>',
        content
    )
    
    # Update all navigation links from ../ru/ to ../en/ and vice versa
    content = content.replace('../ru/', '../en/')
    # But the RU link should still point to ../ru/
    content = re.sub(
        r'<a href="\.\./en/index\.html" class="hover:text-white transition">RU</a>',
        r'<a href="../ru/index.html" class="hover:text-white transition">RU</a>',
        content
    )
    
    # Apply simple term translations for navigation
    for ru, en in TRANSLATIONS.items():
        # Be careful with replacements - use word boundaries where appropriate
        content = content.replace(f'>{ru}<', f'>{en}<')
        content = content.replace(f'"{ru}"', f'"{en}"')
    
    # Note: Full content translation will be done manually or with AI
    # This script creates the structure and updates the template parts
    
    # Write translated content
    os.makedirs(output_path.parent, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {output_path}")

def main():
    """Main translation function."""
    ru_dir = Path("/home/runner/work/books.github.io/books.github.io/book_clean_architecture/ru")
    en_dir = Path("/home/runner/work/books.github.io/books.github.io/book_clean_architecture/en")
    
    # Create en directory if it doesn't exist
    en_dir.mkdir(exist_ok=True)
    
    # Get all HTML files
    html_files = sorted(ru_dir.glob("*.html"))
    
    print(f"Found {len(html_files)} HTML files to translate")
    
    for html_file in html_files:
        output_file = en_dir / html_file.name
        translate_file(html_file, output_file)
    
    print(f"\nTranslation structure complete! Created {len(html_files)} files in {en_dir}")
    print("\nNote: This script created the file structure and translated navigation.")
    print("Full content translation needs to be done for each file.")

if __name__ == "__main__":
    main()
