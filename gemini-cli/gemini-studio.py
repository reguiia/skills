#!/usr/bin/env python3

import os
import shutil
from utils import run_command

def create_presentation():
    """Interactive flow to create a new PowerPoint presentation."""
    print("Let's create a new presentation!")

    # Get presentation title
    presentation_title = input("What is the title of your presentation? ")

    # Create a temporary directory for the HTML slides
    temp_dir = "temp_slides"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    print("Now, let's add some slides. Type 'done' when you are finished.")

    slide_number = 1
    while True:
        print(f"\n--- Slide {slide_number} ---")
        slide_title = input("Slide title (or 'done'): ")
        if slide_title.lower() == 'done':
            break

        slide_content = input("Slide content: ")

        # Create the HTML file for the slide
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
          body {{
            width: 960px;
            height: 540px;
            font-family: Arial, sans-serif;
            padding: 20px;
          }}
          h1 {{
            color: #333366;
          }}
          p {{
            font-size: 18px;
          }}
        </style>
        </head>
        <body>
          <h1>{slide_title}</h1>
          <p>{slide_content}</p>
        </body>
        </html>
        """

        with open(os.path.join(temp_dir, f"slide{slide_number}.html"), "w") as f:
            f.write(html_content)

        slide_number += 1

    print("\nGenerating presentation...")

    # Generate the presentation
    output_file = f"{presentation_title.replace(' ', '_')}.pptx"
    run_command(f"python3 gemini_pptx.py create {temp_dir} {output_file}")

    # Clean up the temporary directory
    shutil.rmtree(temp_dir)

    print(f"\nPresentation '{output_file}' created successfully!")


def main():
    """Main function to run the conversational CLI."""
    print("Welcome to Gemini Studio!")
    print("What would you like to do?")
    print("1. Create a new presentation")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        create_presentation()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
