#!/usr/bin/env python3
"""
Test GUI Loading
"""

import sys
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

try:
    from aetherra.ui.aetherplex import AetherraWindow

    print("✅ GUI classes loaded successfully")

    # Test initialization without actually showing GUI
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    window = AetherraWindow()
    print("✅ GUI window initialized successfully")
    print("🧠 Memory timeline feature added")
    print("🚀 Ready to launch GUI")

except Exception as e:
    print(f"❌ Error loading GUI: {e}")
    import traceback

    traceback.print_exc()
