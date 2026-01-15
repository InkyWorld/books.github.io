#!/usr/bin/env python3
"""
Script to translate Russian navigation text to English in HTML files
"""
import re
from pathlib import Path

# Navigation translations
NAV_TRANSLATIONS = {
    # Fundamentals
    "Введение": "Introduction",
    "SOLID принципы": "SOLID Principles",
    "Структура проекта (DDD)": "Project Structure (DDD)",
    
    # Tactical DDD
    "Инварианты": "Invariants",
    
    # CQRS & Distributed Systems section
    "CQRS и Распределенные системы": "CQRS & Distributed Systems",
    "CQRS и ES": "CQRS & ES",
    
    # Reliability & Security section
    "Надежность и Безопасность": "Reliability & Security",
    
    # Quality & Practice section
    "Качество и Практика": "Quality & Practice",
    "Тестирование": "Testing",
    "Избыточность": "Overengineering",
    "Мини-проекты": "Mini Projects",
    "Антипаттерны": "Antipatterns",
    
    # About section
    "О проекте": "About",
    "Послесловие": "Afterword",
    
    # Navigation footer
    "Назад": "Previous",
    "Далее": "Next",
}

def translate_file(filepath):
    """Translate navigation text in a single file"""
    content = filepath.read_text(encoding='utf-8')
    modified = False
    
    for russian, english in NAV_TRANSLATIONS.items():
        old_content = content
        # Escape special regex characters
        russian_escaped = re.escape(russian)
        content = re.sub(russian_escaped, english, content)
        if content != old_content:
            modified = True
            print(f"  Replaced: {russian} -> {english}")
    
    if modified:
        filepath.write_text(content, encoding='utf-8')
        print(f"✓ Updated: {filepath.name}")
        return True
    else:
        print(f"- No changes: {filepath.name}")
        return False

def main():
    en_dir = Path("book_clean_architecture/en")
    files_to_translate = [
        "acl.html", "advanced_techniques.html", "afterword.html", "antipatterns.html",
        "background_tasks.html", "big_ball_of_mud.html", "boundaries_first.html",
        "concurrency.html", "config_logging.html", "context_map.html",
        "context_relationships.html", "cqrs_es.html", "deployment.html",
        "domain_events.html", "error_handling.html", "event_storming.html",
        "frameworks_django.html", "middleware.html", "modular_monolith.html",
        "observability.html", "outbox.html", "overengineering.html",
        "policies.html", "projects.html", "repository_uow.html",
        "saga.html", "security.html", "specification.html",
        "strategic_distillation.html", "subdomains.html", "testing.html",
        "ubiquitous_language.html", "versioning.html"
    ]
    
    updated_count = 0
    for filename in files_to_translate:
        filepath = en_dir / filename
        if filepath.exists():
            print(f"\n Processing {filename}...")
            if translate_file(filepath):
                updated_count += 1
        else:
            print(f"! File not found: {filename}")
    
    print(f"\n✅ Translation complete! Updated {updated_count} files.")

if __name__ == "__main__":
    main()
