#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Aetherra Project - Main Launcher
=================================

Unified launcher for the newly organized and modularized Aetherra project.
Provides easy access to all major components.
"""

import os
import sys
from pathlib import Path

# Add src to Python path
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))


def print_banner():
    """Print Aetherra banner."""
    print("🧬" + "=" * 60 + "🧬")
    print("🚀 Aetherra Project - AI-Native Programming Language 🚀")
    print("📦 Version 2.1.0 - Modular Architecture")
    print("🧬" + "=" * 60 + "🧬")
    print()


def print_menu():
    """Print main menu options."""
    print("🎯 Available Options:")
    print("  1. 🧬  Launch Lyrixa (AI-Native Development Environment)")
    print("  2. 🎮  Launch Aetherra Playground")
    print("  3. 🧪  Verify Components")
    print("  4. 📊  Show Project Structure")
    print("  5. 🔧  Run CLI Interface")
    print("  6. ❓  Help & Documentation")
    print("  0. 🚪  Exit")
    print()


def show_project_structure():
    """Show the new project structure."""
    print("📁 Aetherra Project Structure:")
    print("├── src/aetherra/           # Core package")
    print("│   ├── core/                # Core engine")
    print("│   │   ├── parser/          # Parser subsystem")
    print("│   │   ├── ast/             # AST components")
    print("│   │   ├── interpreter/     # Interpreter subsystem")
    print("│   │   ├── memory/          # Memory systems")
    print("│   │   ├── ai/              # AI integration")
    print("│   │   └── utils/           # Core utilities")
    print("│   ├── ui/                  # Modular UI components")
    print("│   ├── plugins/             # Plugin system")
    print("│   ├── stdlib/              # Standard library")
    print("│   └── cli/                 # CLI interface")
    print("├── launchers/               # Application launchers")
    print("├── scripts/                 # Development scripts")
    print("├── tests/                   # Test suite")
    print("├── examples/                # Example programs")
    print("├── docs/                    # Documentation")
    print("├── data/                    # Data files")
    print("└── archive/                 # Legacy files")
    print()


def main():
    """Main launcher function."""
    print_banner()

    while True:
        print_menu()
        choice = input("🎯 Choose an option (0-6): ").strip()

        try:
            if choice == "0":
                print("👋 Goodbye! Thank you for using Aetherra!")
                break

            elif choice == "1":
                print("🚀 Launching Lyrixa...")
                print("💡 Features:")
                print("   • Integrated AI chat assistant")
                print("   • Modern dark mode interface")
                print("   • Unified development environment")
                print("   • AI-native programming workflow")
                input("\n📍 Press Enter to continue...")
                try:
                    os.system(f'python "{project_root}/launchers/launch_lyrixa.py"')
                except Exception as e:
                    print(f"❌ Error launching Lyrixa: {e}")

            elif choice == "2":
                print("🎮 Launching Aetherra Playground...")
                try:
                    os.system(f'python "{project_root}/launchers/launch_playground.py"')
                except Exception as e:
                    print(f"❌ Error launching playground: {e}")

            elif choice == "3":
                print("🧪 Verifying Modular Components...")
                try:
                    os.system(
                        f'python "{project_root}/scripts/tools/verify_modular_components.py"'
                    )
                except Exception as e:
                    print(f"❌ Error running verification: {e}")

            elif choice == "4":
                show_project_structure()

            elif choice == "5":
                print("🔧 Launching CLI Interface...")
                try:
                    from aetherra.cli.main import main as cli_main

                    cli_main()
                except Exception as e:
                    print(f"❌ Error launching CLI: {e}")

            elif choice == "6":
                print("📚 Aetherra Documentation:")
                print("  • Architecture: docs/MODULAR_ARCHITECTURE.md")
                print("  • Installation: docs/guides/INSTALLATION.md")
                print("  • Tutorial: docs/guides/TUTORIAL.md")
                print("  • API Docs: docs/api/")
                print("  • Language Spec: docs/AETHERRA_LANGUAGE_SPEC.md")
                print()

            else:
                print("❌ Invalid choice. Please enter 0-6.")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

        input("\n📍 Press Enter to continue...")
        print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    sys.exit(main())


if __name__ == "__main__":
    sys.exit(main())
