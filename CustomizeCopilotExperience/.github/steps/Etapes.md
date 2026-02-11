[Uploading 1-step.md…]()
## Step 1: Setting Up Copilot Instructions

You're a teacher at Mergington High School who creates homework assignments and coding exercises for students. You maintain a static website to share these assignments and want to establish general standards for AI assistants to ensure consistent code quality and project structure.

You've heard Copilot Instructions can help with that!

<details>
<summary>Website screenshot 📸</summary><br/>

You will run this website in the first activity!

<img width="600" alt="screenshot of homework website" src="https://github.com/user-attachments/assets/2383b6e9-64d5-4907-94b3-b67153efb008" />

</details>

### 📖 Theory: What are repository custom instructions?

Repository custom instructions let you provide Copilot with repository-specific guidance and preferences that help it understand your project context and standards. By creating a `.github/copilot-instructions.md` file, you can ensure that Copilot's suggestions consistently follow your project conventions and coding standards.

The complete set of instructions will be automatically added to all requests that you submit to Copilot Chat in your repository.

> [!TIP]
> Keep instructions short and focused on the "how" of the project. This could be purpose, folder structure, coding standards, key tools, expected formats, etc.

See the [GitHub Docs: Repository Custom Instructions](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) page for more information.

### ⌨️ Activity: Explore the Educational Website Project

To work with custom instructions, let's first set up our development environment and explore the project structure.

1. Right-click the below button to open the **Create Codespace** page in a new tab. Use the default configuration.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirm the **Repository** field is your copy of the exercise, not the original, then click the green **Create Codespace** button.

   - ✅ Your copy: `/{{full_repo_name}}`
   - ❌ Original: `/skills/customize-your-github-copilot-experience`

1. Wait a moment for Visual Studio Code to load in your browser and for all extensions to install.

   - Ensure the **Live Preview** extension is activated.
   - Ensure the **Python** extension is activated.

1. Right-click on `index.html` and select **Show Preview** to see the website in action.

   > ❕ **Important**: Keep the preview tab open to see the live updates. We will be making edits throughout the exercise.

1. Explore the project structure:

   - Browse the `assets/` folder to see the website assets (CSS, JavaScript, images).
   - Look at the `assignments/` folder to understand the existing assignment formats.
   - Review `index.html` in the root directory to see the main website structure.
   - Review `config.json` in the root directory to see how the assignments are set up.

### ⌨️ Activity: Create Repository Copilot Instructions

Now that you've explored the project, let's create custom instructions to help Copilot understand your educational website project.

1. In VS Code, create a new file called:

   ```text
   .github/copilot-instructions.md
   ``` 

   > ❕ **Important:** Make sure the file name is correct. This specific filename is required for Copilot to recognize it.

1. Add the following content so Copilot understands the project's purpose, structure, and requirements:

   ```markdown
   # Project Description

   This project is an educational website for sharing homework assignments and coding exercises with students. Students can browse, view, and download assignments directly from the portal.

   ## Project Structure

   - [`assignments/`](../assignments/) Each homework assignment is stored in its own subfolder with a consistent structure.
   - [`templates/`](../templates/) Reusable templates for new content
   - [`assets/`](../assets/) Contains the website assets including CSS, JavaScript, images, and configuration files
   - [`index.html`](../index.html) The main website page that serves as a static portal for browsing and viewing assignments. Content is configurable via [`config.json`](../config.json) file to dynamically generate assignment lists and details.

   ## Project Guidelines

   - Maintain consistent styling across all pages
   - Keep file and folder names descriptive and organized

   ## Educational Standards

   When generating content for this project:

   - **Learning-focused**: All content should be designed with clear learning objectives and appropriate difficulty levels
   - **Student-friendly**: Use clear, encouraging language that motivates students
   ```

1. Test your instructions by asking Copilot about the project:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Briefly explain this project to me
   > ```

1. Notice that Copilot uses your custom instructions as a reference in the response.

   <img width="504" height="183" alt="image" src="https://github.com/user-attachments/assets/2214ed9e-c165-4440-a23e-d2d33c0231a9" />

1. Commit the `.github/copilot-instructions.md` file to the `main` branch and push it to GitHub.

1. Wait for Mona to prepare the next step!

<details>
<summary>Having trouble? 🤷</summary><br/>

- The `.github/copilot-instructions.md` file should be at the root of the `.github` folder
- Make sure you committed and pushed the changes.

</details>

## Step 2: File-Specific Instructions

With the general project instructions ready, you realize you need more specific formatting rules related to just the assignments. While your repository-wide instructions work great for general coding standards, you don't want to clutter them with detailed assignment structure requirements that get included in every chat message.

You want to make sure all your assignments follow the same pattern and structure so students have a consistent experience, but these rules should only apply when working on assignment files.

### 📖 Theory: Custom Instruction Files

Instruction files (`*.instructions.md`) provide Copilot targeted guidance for specific files or directories in your project.

Unlike repository-wide instructions that apply everywhere, these files use the `applyTo` field in the [frontmatter](https://jekyllrb.com/docs/front-matter/) using [glob syntax](https://code.visualstudio.com/docs/editor/glob-patterns) to target specific files. This automatically applies the instructions whenever Copilot works on files matching that pattern. Alternatively, you can manually attach instructions using the **Add Context** button in Copilot Chat.

Visual Studio Code will look for `*.instructions.md` files in `.github/instructions/` directory by [default](vscode://settings/chat.instructionsFilesLocations).

> [!TIP]
> Instructions should focus on **HOW** a task should be done - describing the guidelines, standards, and conventions used in that particular part of the codebase

See the [VS Code Docs: Custom Instructions](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions) page for more information.

### ⌨️ Activity: Create Assignment-Specific Instructions

Now let's create targeted instructions specifically for assignment files to ensure they follow consistent structure and formatting.

1. First, let's examine the existing assignment template. Open `templates/assignment-template.md` to see the structure we want all assignments to follow.

1. Create a new file called:

   ```text
   .github/instructions/assignments.instructions.md
   ```


1. Add the following content to define assignment formatting standards. It will also ensure they are automatically applied for every chat request to Markdown (`.md`) files in `assignments` directory.

   ```markdown
   ---
   applyTo: "assignments/**/*.md"
   ---

   # Assignment Markdown Structure Guidelines

   All assignment markdown files should follow these guidelines:

   ## 1. Template Usage

   - Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
   - The assignment must be created as a `README.md` file
   - Do not remove or skip required sections from the template.

   ## 2. Section Guidance

   The section headers should reflect the structure in the template, including the exact icon usage.

   - **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
   - **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
   - **Tasks**: For each task:
      - Use a specific, action-oriented task name
      - In the Description, clearly state what the student must do.
      - In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable
      - Provide example input/output in code blocks if helpful.

   Do not include extra sections unless explicitly specified.
   ```

### ⌨️ Activity: Test the Assignment Instructions

1. Open the file `assignments/games-in-python/README.md` in VS Code. This assignment doesn't match all the conventions you've setup as a teacher.

1. Take a moment to review the current structure of this assignment file. Notice how it differs from the template structure you examined earlier. You can also view how it currently appears on the **Site Preview** tab.

1. With the assignment file open, ask Copilot in `Agent` mode to update the assignment structure:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Update this assignment file to follow the project standards and template structure
   > ```

1. Observe how Copilot references the general project instructions and the assignment specific instruction files.

   <img width="492" height="376" alt="screenshot of Copilot chat showing attached references" src="https://github.com/user-attachments/assets/dbf26be3-5940-4619-af4e-0a4380f16494" />

1. Compare the suggested changes with the original file structure to see how Copilot applied your instructions. Apply the suggested changes and check how the updated assignment now appears on the **Site Preview**.

1. Commit both files to the `main` branch and push your changes to GitHub.

   - `.github/instructions/assignments.instructions.md`
   - `assignments/games-in-python/README.md`

1. Wait for Mona to prepare the next step!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure you committed both files to `main` branch:
  - `.github/instructions/assignments.instructions.md`
  - `assignments/games-in-python/README.md`

</details>

## Step 3: Building Reusable Prompts

Now that you've established instructions for assignments, you want to streamline creating new assignments.

Creating assignments is a repetitive task and involves multiple steps, a perfect scenario for a reusable prompt!

- Creating the assignment
- Updating the website configuration to load the new assignment

### 📖 Theory: Prompt Files

Prompt files (`*.prompt.md`) are reusable prompts to simplify common and useful tasks in your project. They are selected in Copilot Chat using slash commands (`/`).

They can reference other workspace files, prompt files, or instructions files by using Markdown-style links relative to the prompt file location.

Visual Studio Code will look for `*.prompt.md` files in `.github/prompts/` directory by [default](vscode://settings/chat.promptFilesLocations).

> [!TIP]
> Use prompt files to define repeatable tasks and workflows.
>
> When writing prompts focus on **WHAT** needs to be done. You can reference instructions for the **HOW**.

See the [VS Code Docs: Prompt Files](https://code.visualstudio.com/docs/copilot/copilot-customization#_prompt-files-experimental) page for more information.

### ⌨️ Activity: Create an Assignment Prompt

Now let's create a reusable prompt that automates the entire assignment creation process. This is perfect for a prompt file because creating assignments involves multiple repetitive steps that follow the same pattern every time - exactly the kind of workflow that benefits from automation.

1. Create a new file called:

   ```text
   .github/prompts/new-assignment.prompt.md
   ```

1. Add the following content to create a comprehensive assignment generation prompt:

   ```markdown
   ---
   agent: agent
   description: Create a new programming homework assignment
   argument-hint: Provide assignment details
   ---

   # Create New Programming Assignment

   Your goal is to generate a new homework assignment for the Mergington High School students.

   ## Step 1: Gather Assignment Information

   If not already provided by the user, ask what the assignment will be about.

   ## Step 2: Create Assignment Structure

   1. Create a new directory in the `assignments` folder with a unique name based on the assignment topic
   1. Create a new file in the directory named `README.md` with the structure from the [assignment-template.md](../../templates/assignment-template.md) file
   1. Fill out the assignment details in the README file
   1. (Optional) Add starter code or attachments if the assignment needs them - add these files to the same assignment folder

   ## Step 3: Update Website Configuration

   Update the assignments list in [config.json](../../config.json) website configuration file to include the new assignment. For the dueDate field, use the current date plus 7 days unless specified otherwise.
   ```

### ⌨️ Activity: Test the Assignment Prompt

1. Open Copilot Chat in VS Code and ensure you're in `Agent` mode.

1. Run your prompt by typing `/new-assignment` in the chat input. There are 2 options:

   - Type just `/new-assignment` without a description. Copilot will ask what the assignment should be about.
   - Include the topic directly: `/new-assignment Building REST APIs with FastAPI framework`

      <details>
      <summary>💡 Assignment Topic Ideas</summary>

      ```text
      Python Text Processing - working with strings, file I/O, and text manipulation
      ```

      ```text
      Data Structures in Python - lists, dictionaries, sets, and tuples
      ```

      ```text
      Python Data Visualization - using matplotlib or plotly for charts and graphs
      ```

      ```text
      Building REST APIs with FastAPI framework
      ```

      ```text
      Statistics with Python - data analysis and statistical calculations using pandas and numpy
      ```

      </details>

1. Verify the new assignment appears in the assignments list on the website preview.

   <details>
   <summary>Assignment not showing? 🔍</summary>

   Check these items:

   - Refresh the page.
   - A new directory was created in `assignments/`.
   - The `config.json` file was updated with the new assignment.

   </details>

1. Review the generated assignment content to ensure it matches your established conventions.

1. Commit and push your changes:

   - The new prompt file: `.github/prompts/new-assignment.prompt.md`
   - The generated assignment directory and files.
   - Updated `config.json` configuration.

1. Wait for Mona to prepare the next step!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the prompt file is in the `.github/prompts/` directory with the `.prompt.md` extension.

</details>

## Step 4: Creating Custom Agents

Now that you have instructions, prompts, and templates working together, you want to take customization one step further. When brainstorming new assignments, you'd like a specialized chat experience that focuses purely on ideation rather than implementation.

### 📖 Theory: Custom Agents

Custom agents (`*.agent.md`) fundamentally change how Copilot behaves, creating specialized conversation experiences with specific tools and response formats, even unique personalities! They are selected from a dropdown list in the Copilot Chat interface.

Visual Studio Code will look for `*.agent.md` files in `.github/agents/` directory.

> [!TIP]
> Learn more about Custom Agents:
>
> - [VS Code Docs: Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
> - [GitHub Docs: Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)


### ⌨️ Activity: Create an Assignment Brainstorming Custom Agent

Now let's create a specialized custom agent for brainstorming assignment ideas.

1. Create a new file called:

   ```text
   .github/agents/assignment-brainstorming.agent.md
   ```

1. Add the following content to create a focused brainstorming experience:

   ```markdown
   ---
   name: assignment-brainstorming
   description: Assignment brainstorming assistant
   tools: ["search", "fetch"]
   ---

   # 💡 Assignment Brainstorming Assistant

   **BRAINSTORM MODE ACTIVATED** 🚀

   I'm your assignment brainstorming partner for Mergington High School! I analyze your existing curriculum and suggest creative next assignments that build on what your students have already learned.

   ## My Response Style

   Every response follows this format:

   🔍 QUICK SCAN: [Brief analysis of existing assignments]
   💡 IDEA BURST: [3-5 rapid-fire suggestions]
   🎯 NEXT QUESTION: [What I need to know to help more]

   ## Rules

   - ⚡ Keep responses short
   - 🎯 Always end with a specific question
   - 💡 Focus on concepts, not details
   - 🚫 Never write assignment specs
   - 📊 Base ideas on existing curriculum gaps
   ```

### ⌨️ Activity: Test the Brainstorming Custom Agent

1. Open Copilot Chat in VS Code.

1. Select your custom agent from the agent dropdown list.

   <img width="379" height="218" alt="copilot agent: assignment brainstorming agent selected" src="https://github.com/user-attachments/assets/4effffa7-b8ef-4830-8050-9c777f9f0189" />

1. Test the custom agent with questions a teacher might ask. Notice the different response format!

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > What assignment topics are missing from my current curriculum?
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Suggest 3 advanced Python assignments for my students.
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > What would be a good follow-up assignment after the data analysis assignment?
   > ```

1. Try asking follow-up questions to see how the custom agent maintains its personality throughout the conversation.

1. Commit and push your changes for the new custom agent file: `.github/agents/assignment-brainstorming.agent.md`

1. Wait for Mona to give you a final review!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the custom agent file is in `.github/agents/` directory with the `.agent.md` extension.
- Custom agents are selected from the dropdown list at the bottom of the chat interface, not with `@` mentions.
- If the custom agent doesn't appear in the dropdown, restart VS Code or reload the window.

</details>

## Review

_Congratulations, you've completed this exercise and learned how to customize GitHub Copilot!_

<img src="https://octodex.github.com/images/jetpacktocat.png" alt="celebrate" width=200 align=right>

Here's a recap of your accomplishments:

- Set up repository-wide custom instructions to ensure consistent code generation
- Created targeted custom instructions for specific file types and directories
- Built reusable prompt templates for common tasks like homework assignments
- Configured custom agents for specialized workflows

### What's next?

Take another GitHub Skills exercise on [GitHub Learn](https://learn.github.com/skills):

- [Integrate MCP with Copilot](https://github.com/skills/integrate-mcp-with-copilot) - Learn how to extend Copilot with Model Context Protocol. You will learn about MCP tools which can also be used in custom agents and prompts!
- [Modernize Legacy Code](https://github.com/skills/modernize-your-legacy-code-with-github-copilot) - Use Copilot to help refactor and improve existing codebases.
- [GitHub Pages](https://github.com/skills/github-pages) - Learn how to publish static website's like the one in this exercise.
