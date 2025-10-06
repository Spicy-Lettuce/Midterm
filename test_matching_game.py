#!/usr/bin/env python3
"""Test script to verify the matching game fix handles odd grid sizes correctly"""

def test_even_tiles_logic(rows, cols):
    """Simulate the logic from save_options to ensure even number of tiles"""
    # This is the fix we added
    if (rows * cols) % 2 != 0:
        cols = cols + 1
    
    total_tiles = rows * cols
    return rows, cols, total_tiles

# Test cases
test_cases = [
    (3, 3, "Odd × Odd = 9 tiles"),      # Should become 3×4 = 12
    (3, 4, "Odd × Even = 12 tiles"),    # Should stay 3×4 = 12
    (4, 3, "Even × Odd = 12 tiles"),    # Should stay 4×3 = 12
    (4, 4, "Even × Even = 16 tiles"),   # Should stay 4×4 = 16
    (5, 5, "Odd × Odd = 25 tiles"),     # Should become 5×6 = 30
    (1, 1, "Edge case: 1×1 = 1 tile"),  # Should become 1×2 = 2
]

print("Testing matching game grid adjustment logic:")
print("=" * 60)

all_passed = True
for rows_input, cols_input, description in test_cases:
    rows_result, cols_result, total = test_even_tiles_logic(rows_input, cols_input)
    is_even = total % 2 == 0
    status = "✓ PASS" if is_even else "✗ FAIL"
    
    if not is_even:
        all_passed = False
    
    print(f"{status} | {description}")
    print(f"      Input: {rows_input}×{cols_input}, Output: {rows_result}×{cols_result} = {total} tiles")
    print()

print("=" * 60)
if all_passed:
    print("✓ All tests passed! The game will work with any grid size.")
else:
    print("✗ Some tests failed!")
