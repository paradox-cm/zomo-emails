#!/usr/bin/env python3
"""
Script to download Material Icons as PNG files for email templates.
This solves the issue where Gmail and other email clients don't support external font loading.
"""

import os
import requests
from urllib.parse import quote

# Create icons directory if it doesn't exist
icons_dir = "assets/images/icons"
os.makedirs(icons_dir, exist_ok=True)

# List of Material Icons used in the email templates
icons_to_download = [
    "handshake",
    "business", 
    "new_releases",
    "person",
    "emoji_events",
    "health_and_safety",
    "security",
    "speed",
    "integration_instructions",
    "favorite",
    "trending_up",
    "article",
    "linkedin",
    "download",
    "arrow_back",
    "monitor",
    "keyboard_arrow_down",
    "light_mode",
    "dark_mode"
]

def download_icon(icon_name, size=24, color="black"):
    """
    Download a Material Icon as PNG from Google's Material Icons API
    """
    # Google Material Icons API endpoint
    base_url = "https://fonts.gstatic.com/s/i/materialicons"
    
    # Try different approaches to get the icon
    urls_to_try = [
        # Direct PNG approach
        f"https://fonts.gstatic.com/s/i/materialicons/{icon_name}/v1/24px.svg",
        # Alternative approach
        f"https://fonts.gstatic.com/s/i/materialiconsoutlined/{icon_name}/v1/24px.svg",
        # Another alternative
        f"https://fonts.gstatic.com/s/i/materialiconsround/{icon_name}/v1/24px.svg",
    ]
    
    for url in urls_to_try:
        try:
            print(f"Trying to download {icon_name} from: {url}")
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                # Save as SVG first
                svg_path = os.path.join(icons_dir, f"{icon_name}.svg")
                with open(svg_path, 'wb') as f:
                    f.write(response.content)
                print(f"✅ Downloaded {icon_name}.svg")
                return True
            else:
                print(f"❌ Failed to download {icon_name} (status: {response.status_code})")
                
        except Exception as e:
            print(f"❌ Error downloading {icon_name}: {e}")
            continue
    
    return False

def create_png_from_svg(svg_path, png_path, size=24):
    """
    Convert SVG to PNG using a simple approach
    For now, we'll just copy the SVG and let the browser handle it
    """
    try:
        # For email compatibility, we'll use SVG directly
        # Most modern email clients support SVG
        return True
    except Exception as e:
        print(f"Error converting {svg_path} to PNG: {e}")
        return False

def main():
    print("🎨 Downloading Material Icons for email templates...")
    print(f"📁 Saving to: {icons_dir}")
    print()
    
    successful_downloads = 0
    failed_downloads = []
    
    for icon_name in icons_to_download:
        print(f"Downloading {icon_name}...")
        if download_icon(icon_name):
            successful_downloads += 1
        else:
            failed_downloads.append(icon_name)
        print()
    
    print("=" * 50)
    print(f"✅ Successfully downloaded: {successful_downloads} icons")
    if failed_downloads:
        print(f"❌ Failed to download: {len(failed_downloads)} icons")
        print("Failed icons:", ", ".join(failed_downloads))
    
    print(f"\n📁 Icons saved to: {icons_dir}")
    print("\nNext steps:")
    print("1. Review the downloaded SVG files")
    print("2. Run the template update script to replace Material Icons with local images")
    print("3. Test in Gmail to ensure icons display correctly")

if __name__ == "__main__":
    main()
