#!/usr/bin/env python3
"""
Script to fix duplicate attributes in the email templates after icon replacement.
"""

import os
import re
import glob

def fix_duplicate_attributes(file_path):
    """
    Fix duplicate attributes in a template file
    """
    print(f"🔧 Fixing {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match img tags with duplicate attributes
        # Look for img tags that have duplicate style attributes or malformed attributes
        pattern = r'<img src="assets/images/icons/[^"]*\.svg"[^>]*style="[^"]*"[^>]*font-size:[^>]*>'
        
        def fix_img_tag(match):
            img_tag = match.group(0)
            
            # Extract the src and alt attributes
            src_match = re.search(r'src="([^"]*)"', img_tag)
            alt_match = re.search(r'alt="([^"]*)"', img_tag)
            
            if not src_match:
                return img_tag  # Return original if we can't parse it
            
            src = src_match.group(1)
            alt = alt_match.group(1) if alt_match else ""
            
            # Extract the clean style attribute (the first one)
            style_match = re.search(r'style="([^"]*)"', img_tag)
            if style_match:
                style = style_match.group(1)
                # Clean up the style - remove any malformed parts
                style = re.sub(r'font-size:[^;]*;?', '', style)
                style = re.sub(r';;+', ';', style)  # Remove double semicolons
                style = style.strip(';')
            else:
                style = "width:16px; height:16px; vertical-align:middle;"
            
            return f'<img src="{src}" alt="{alt}" style="{style}">'
        
        # Fix the img tags
        content = re.sub(pattern, fix_img_tag, content)
        
        # Also fix any remaining malformed img tags
        content = re.sub(r'<img src="([^"]*)" alt="([^"]*)" style="([^"]*)"[^>]*font-size:[^>]*>', 
                        r'<img src="\1" alt="\2" style="\3">', content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed {file_path}")
            return True
        else:
            print(f"ℹ️  No fixes needed for {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False

def main():
    print("🔧 Fixing duplicate attributes in email templates...")
    print()
    
    # Find all HTML template files
    template_files = glob.glob("emails/newsletters/*.html")
    
    if not template_files:
        print("❌ No template files found")
        return
    
    fixed_count = 0
    
    for template_file in template_files:
        if fix_duplicate_attributes(template_file):
            fixed_count += 1
        print()
    
    print("=" * 50)
    print(f"✅ Successfully fixed {fixed_count} template files")

if __name__ == "__main__":
    main()
