#!/usr/bin/env python3
"""
Script to fix remaining Material Icons that weren't replaced with img tags.
"""

import os
import re
import glob

# Base URL for the Vercel deployment
BASE_URL = "https://zomo-emails.vercel.app"

# Mapping of Material Icon names to their SVG file paths
icon_mapping = {
    "handshake": "assets/images/icons/handshake.svg",
    "business": "assets/images/icons/business.svg", 
    "new_releases": "assets/images/icons/new_releases.svg",
    "person": "assets/images/icons/person.svg",
    "emoji_events": "assets/images/icons/emoji_events.svg",
    "health_and_safety": "assets/images/icons/health_and_safety.svg",
    "security": "assets/images/icons/security.svg",
    "speed": "assets/images/icons/speed.svg",
    "integration_instructions": "assets/images/icons/integration_instructions.svg",
    "favorite": "assets/images/icons/favorite.svg",
    "trending_up": "assets/images/icons/trending_up.svg",
    "article": "assets/images/icons/article.svg",
    "linkedin": "assets/images/icons/linkedin.svg",
    "download": "assets/images/icons/download.svg",
    "arrow_back": "assets/images/icons/arrow_back.svg",
    "monitor": "assets/images/icons/monitor.svg",
    "keyboard_arrow_down": "assets/images/icons/keyboard_arrow_down.svg",
    "light_mode": "assets/images/icons/light_mode.svg",
    "dark_mode": "assets/images/icons/dark_mode.svg",
    "local_shipping": "assets/images/icons/local_shipping.svg",
    "content_copy": "assets/images/icons/content_copy.svg"
}

def create_icon_img_tag(icon_name, style_attrs=""):
    """
    Create an img tag for the icon with proper styling
    """
    if icon_name not in icon_mapping:
        print(f"⚠️  Warning: No local icon found for '{icon_name}'")
        return f'<span class="material-icons" {style_attrs}>{icon_name}</span>'
    
    svg_path = f"{BASE_URL}/{icon_mapping[icon_name]}"
    
    # Extract style attributes from the original span
    style_match = re.search(r'style="([^"]*)"', style_attrs)
    if style_match:
        original_style = style_match.group(1)
        # Convert font-size to width/height for img tag
        width_height = "16px"  # default
        if "font-size:24px" in original_style:
            width_height = "24px"
        elif "font-size:32px" in original_style:
            width_height = "32px"
        elif "font-size:12px" in original_style:
            width_height = "12px"
        
        # Preserve color and other important styles
        color_match = re.search(r'color:([^;]+)', original_style)
        color = color_match.group(1) if color_match else "currentColor"
        
        # Create new style for img tag
        new_style = f'width:{width_height}; height:{width_height}; vertical-align:middle; color:{color};'
        
        # Add margin if present
        margin_match = re.search(r'margin-right:([^;]+)', original_style)
        if margin_match:
            new_style += f' margin-right:{margin_match.group(1)};'
    else:
        new_style = "width:16px; height:16px; vertical-align:middle;"
    
    return f'<img src="{svg_path}" alt="{icon_name}" style="{new_style}">'

def fix_remaining_icons(file_path):
    """
    Fix remaining Material Icons in a template file
    """
    print(f"🔧 Fixing remaining icons in {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match remaining Material Icons spans
        # Matches: <span class="material-icons" ...>icon_name</span>
        pattern = r'<span class="material-icons([^>]*)>([^<]+)</span>'
        
        def replace_icon(match):
            style_attrs = match.group(1)
            icon_name = match.group(2).strip()
            
            # Skip if it's not a known icon
            if icon_name not in icon_mapping:
                return match.group(0)  # Return original
            
            return create_icon_img_tag(icon_name, style_attrs)
        
        # Replace all remaining Material Icons with local SVG images
        content = re.sub(pattern, replace_icon, content)
        
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
    print("🔧 Fixing remaining Material Icons in email templates...")
    print(f"Base URL: {BASE_URL}")
    print()
    
    # Find all HTML template files
    template_files = glob.glob("emails/newsletters/*.html")
    
    if not template_files:
        print("❌ No template files found")
        return
    
    fixed_count = 0
    
    for template_file in template_files:
        if fix_remaining_icons(template_file):
            fixed_count += 1
        print()
    
    print("=" * 50)
    print(f"✅ Successfully fixed {fixed_count} template files")
    print()
    print("All Material Icons should now be replaced with img tags!")

if __name__ == "__main__":
    main()
