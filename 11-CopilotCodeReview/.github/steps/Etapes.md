## Step 1: Ask for a Review in VS Code

Mergington High School has an Extracurricular Activities website. In the last months, you have added lots of features and it has become increasingly well used by your fellow staff and students.

Now, multiple teachers want to help develop new features. This is great, but your energy is limited and if you don't have time to review changes, you fear the application will become messy. To scale your "review" availability, let's implement **GitHub Copilot code review**!

Before we implement automated code reviews with Copilot, it makes sense to try reviews locally in VS Code. This will help us better understand it, build our review criteria, and ensure all teacher-collaborators receive consistent feedback when they start contributing.

### 📖 Theory: GitHub Copilot Local Code Review

GitHub Copilot can review your code directly in VS Code, providing immediate feedback on uncommitted changes. It even adds comments similar to the feedback in a pull request! This local review capability allows developers to catch issues before they even reach version control, improving code quality from the start. And maybe catch those embarrassing typos! 😅

Key features:

- **Local analysis** of uncommitted changes
- **Code quality and style** recommendations
- **Detection** of common security vulnerabilities
- **Performance optimization** suggestions

This immediate feedback helps you identify and fix issues early in your development process, making your code more robust before it even reaches a pull request.

## ⌨️ Activity: Get to know the extracurricular activities site

Before we start developing and reviewing, let's take a moment to understand the current site.

1. Right-click the below button to open the **Create Codespace** page in a new tab. Use the default configuration.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Wait some time for the environment to be prepared. It will automatically install all requirements and services.

1. Validate the **GitHub Copilot** and **Python** extensions are installed and enabled.

   <img width="300" alt="copilot extension for VS Code" src="https://github.com/user-attachments/assets/ef1ef984-17fc-4b20-a9a6-65a866def468" /><br/>
   <img width="300" alt="python extension for VS Code" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />

1. Try running the application. In the left sidebar, select the **Run and Debug** tab and then press the **Start Debugging** icon.

   <img width="300" alt="run and debug" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />

   <details>
   <summary>🤷 Having trouble?</summary><br/>

   If the **Run and Debug** area is empty, try reloading VS Code: Open the command palette (`Ctrl`+`Shift`+`P`) and search for `Developer: Reload Window`.

   <img width="300" alt="empty run and debug panel" src="https://github.com/user-attachments/assets/0dbf1407-3a97-401a-a630-f462697082d6" />

   </details>

1. Use the **Ports** tab to find the webpage address, open it, and verify it is running.

   <img width="350" alt="ports tab" src="https://github.com/user-attachments/assets/8d24d6b5-202d-4109-8174-2f0d1e4d8d44" />

   ![Screenshot of Mergington High School WebApp](https://github.com/user-attachments/assets/5e1e7c1e-1b0e-4378-a5af-a266763e6544)

### ⌨️ Activity: Ask Copilot for a review

Let's add a simple banner feature for teachers to make announcements and then ask Copilot for feedback.

1. In VS Code, create a new branch with the following name.

   ```txt
   add-announcement-banner
   ```

1. Open the `src/static/index.html` file. Add the following after the `<body>` tag.

   ```html
   <div class="announcement-banner">
     📢 Activity registration is open until the end of the month. Don't lose your spot!
   </div>
   ```

1. Open the `src/static/styles.css` file. Add the following to the end.

   ```css
   .announcement-banner {
     background-color: #4caf50;
     color: white;
     text-align: center;
     padding: 15px;
     font-weight: bold;
   }
   ```

1. (optional) Refresh the running app to see the change.

   <img width="400" alt="screenshot of site with announcement banner" src="https://github.com/user-attachments/assets/39de7fe0-58f2-4eba-a163-d3037b2b3b06"/>

1. In VS Code, open the source control panel and ensure there are uncommitted changes.

1. Hover over the **Changes** section to show various icons. Click the **Code Review** button and wait a moment for Copilot to add comments.

   <img width="300" alt="screenshot of site with announcement banner" src="https://github.com/user-attachments/assets/6c52d550-d67b-4af9-99dd-e181695a4933"/>

   > 💡 **TIP:** There are 3 levels of review available: `unstaged changes` and `staged changes` and `uncommitted changes`

1. Expand the **Comments** panel to find a list of review feedback from Copilot.

   <img width="300" alt="screenshot of problems control panel with comments from Copilot" src="https://github.com/user-attachments/assets/64c5efb6-9071-4511-b2a2-2dc85c9e929b"/>

1. Use the **Apply** or **Discard** buttons to address Copilot's feedback.

   <img width="300" alt="screenshot of inline comment with buttons to address feedback" src="https://github.com/user-attachments/assets/aef73097-acaf-4f5b-a52f-52a142bb413f"/>

1. Commit and push the Announcement related changes to the `add-announcement-banner` branch.

1. With your changes pushed, wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Copilot Review in VS Code only considers uncommitted changes. Don't commit before asking for the review.
- If Copilot doesn't provide review feedback, make sure to click the correct review button for the grouping (unstaged, staged, uncommitted).
- If Copilot doesn't see your changes, make sure to save the files first.

</details>

[2-step.md](https://github.com/user-attachments/files/25344580/2-step.md)
## Step 2: Get a Pull Request Review

Now that you've tested Copilot's local review capabilities and made some changes to improve the activities website, it's time to create a pull request and get Copilot's feedback on your proposed changes before they're merged into the main branch, just like one of the other teachers would. Let's see how Copilot reviews changes in the pull request process.

### 📖 Theory: Pull Request Code Reviews

GitHub Copilot analyzes your code and provides intelligent feedback with actionable suggestions you can apply instantly. Each code review consumes one [Premium Request Unit (PRU)](https://docs.github.com/en/copilot/concepts/billing/copilot-requests) from the requester.

> [!IMPORTANT]
> Use [code review responsibly](https://docs.github.com/en/copilot/responsible-use/code-review) - Copilot is trained to be familiar with many common security concerns, but it is not meant to replace dedicated security tools, guidelines, and standards. Please use of the correct tools for the job.

**Key Capabilities:**

- **Automated Analysis**: Reviews code for quality, security, and performance issues
- **Actionable Suggestions**: Provides specific recommendations with suggested code changes
- **Integration**: Works seamlessly with GitHub's native pull request flow, the same as regular peer feedback
- **Non-blocking**: Provides "Comment" reviews that don't block merging or count toward required approvals
- **Customizable**: Supports custom instructions to align with team standards
- **Secure**: Operates within GitHub's secure infrastructure

For more information, see the [GitHub Copilot code review documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review).

### ⌨️ Activity: Request a review

1. If needed, open another web browser tab and navigate to this exercise repository.

1. Start a new pull request. Enter the following details and click the **Create pull request** button.

   - **compare:** `add-announcement-banner`
   - **target:** `main`
   - **title:** `Add announcement banner`

1. In the right-side details area, find the **Reviewers** menu. Click on the **settings icon** to show a list of available reviewers and select **Copilot**.

   <img width="300" alt="screenshot of reviewers menu" src="https://github.com/user-attachments/assets/0f9f2e86-51b7-4542-82a1-afb6a22ab3ca"/>

1. Wait a moment for Copilot to review the changes and add comments to your pull request. Notice an entry was added to the conversation log.

   <img width="300" alt="new log entry - requested review from copilot" src="https://github.com/user-attachments/assets/3e522bda-e68e-4469-93f4-a7ad103cca97"/>

   <img width="500" alt="new log entry - copilot's PR summary" src="https://github.com/user-attachments/assets/0a870950-560e-4df8-80d5-2b93f1be99ab"/>

1. With the review requested, wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If Copilot doesn't appear in the reviewers list, ensure your repository has Copilot enabled
- If Copilot doesn't appear in the reviewers list, check your subscription plan. It is not available for free tier.
- Sometimes reviews take a minute or two to complete.

</details>
[3-step.md](https://github.com/user-attachments/files/25344583/3-step.md)
## Step 3: Customize Your Review

The school's coding standards are crucial for maintaining the activities website. You've noticed that teachers are using different visual styles and coding patterns. With such diverse programming backgrounds and priorities among your teacher-collaborators, let's customize Copilot's review behavior to align with the school's educational programming standards.

### 📖 Theory: Repository Custom Instructions

Repository custom instructions allow you to provide Copilot with context about your project standards and preferences. By creating instruction files, you can ensure Copilot's suggestions consistently follow your team's conventions and focus on your specific requirements. You can even have copilot analyze your project and [generate instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions#_generate-an-instructions-file-for-your-workspace) for you!

**Types of Instructions:**

- **Repository-wide instructions**: Applies to all code in the repository. Ex: `.github/copilot-instructions.md`
- **Path-specific instructions**: Applies to specific files to create focused criteria for different parts of your codebase. Ex: `.github/instructions/NAME.instructions.md`.

Instructions are written in natural language with Markdown format and typically include:

- Security requirements and checklists
- Code standards and conventions
- Performance optimization priorities
- Team-specific preferences and style guides
- Language-specific review criteria

Path-specific instruction files include [YAML front matter](https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter) with file [glob patterns](https://code.visualstudio.com/docs/editor/glob-patterns) to target specific files and directories. Examples:

```yaml
---
applyTo: "tests/**/**,docs/*.md"
---
# Testing Guidelines ...
```

```yaml
---
applyTo: "docs/*.md,README.md"
---
# Documentation Guidelines ...
```

> [!TIP]
> Repository [custom instructions](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) work for both local VS Code code reviews and pull request code reviews, ensuring consistency across your development workflow.

### ⌨️ Activity: Add general instructions

Let's customize Copilot's review considerations by adding custom instructions.

1. In VS Code, ensure you are still on the `add-announcement-banner` branch.

1. Create a file for general repository guidelines.

   File location and name:

   ```txt
   .github/copilot-instructions.md
   ```

   Content:

   ```markdown
   ## Security

   - Validate input sanitization practices.
   - Search for risks that might expose user data.
   - Prefer loading configuration and content from the database instead of hard coded content. If absolutely necessary, load it from environment variables or a non-committed config file.

   ## Code Quality

   - Use consistent naming conventions.
   - Try to reduce code duplication.
   - Prefer maintainability and readability over optimization.
   - If a method is used a lot, try to optimize it for performance.
   - Prefer explicit error handling over silent failures.
   ```

### ⌨️ Activity: Add focused instructions

Let's create specific Copilot's review considerations for the frontend and backend.

1. Create a file for the frontend-specific guidelines.

   > ❗️ **Important**: Make sure to put file-specific instructions in the `.github/instructions/` folder, not the `.github/` folder.

   File location and name:

   ```txt
   .github/instructions/frontend.instructions.md
   ```

   Content:

   ```markdown
   ---
   applyTo: "*.html,*.css,*.js"
   ---

   ## Frontend Guidelines

   - Use accessibility attributes (alt text, aria labels) and color schemes.
   - Use responsive design for compatibility with mobile devices.
   - Validate HTML structure and semantic elements
   ```

1. Create a file for the backend-specific guidelines.

   File location and name:

   ```txt
   .github/instructions/backend.instructions.md
   ```

   Content:

   ```markdown
   ---
   applyTo: "backend/**/*,*.py"
   ---

   ## Backend Guidelines

   - All API endpoints must be defined in the `routers` folder.
   - Load example database content from the `database.py` file.
   - Error handling is only logged on the server. Do not propagate to the frontend.
   - Ensure all APIs are explained in the documentation.
   - Verify changes in the backend are reflected in the frontend (`src/static/**`). If possible breaking changes are found, mention them to the developer.
   ```

1. Commit and push the instruction files.

> [!TIP]
> VS Code has a built-in commands to help manage instructions. Try opening the command pallette and searching for `instructions`.

### ⌨️ Activity: Request another review

With our new instructions defined, Copilot now has a better idea of what is important for our project. Let's ask for another review.

1. In VS Code, Ensure the instructions are indeed committed and push to the repository.

1. In the web browser, return to the recently created pull request.

1. In the top right, find the **Reviewers** menu and **Re-request review** button next to **Copilot**. Click it and wait a moment for Copilot to add comments on the pull request.

   <img width="300" alt="screenshot of re-review button" src="https://github.com/user-attachments/assets/c45aa8de-278d-46e7-bfe2-2dc6b574e11e"/>

   > 🪧 **Note:** If you are too quick after pushing new commits, you may have to wait a moment for the button to appear, or refresh the page.

1. Observe that Copilot's feedback now differs from the previous review.

1. With the review requested, wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If you forgot to add a custom instruction (or made a typo), try fixing the mistake and asking Copilot for another review. This will inform Mona to check your work again.

</details>
[4-step.md](https://github.com/user-attachments/files/25344586/4-step.md)## Step 4: Automate Reviews

The tailored reviews seem to be working great, however there's a problem. They aren't technically required. Manually requesting Copilot reviews clearly isn't sustainable when you have multiple teachers contributing to the activities website. You want every pull request to automatically receive Copilot's feedback, especially since there are varying levels of programming experience among your collaborators. Let's set up repository rulesets to require Copilot reviews on all changes.

### 📖 Theory: Repository Rulesets for Automated Reviews

Repository rulesets allow you to enforce automatic code reviews on all pull requests, ensuring consistent quality checks without relying on developers to manually request reviews or remember to follow documentation.

Each code review consumes one [Premium Request Unit (PRU)](https://docs.github.com/en/copilot/concepts/billing/copilot-requests) from the author of the pull request.

**Enforcement Options:**

- **Repository-level**: All new pull requests in the specific repository
- **Branch-specific**: Target specific branches by filters and name patterns
- **Organization-level**: Apply rule sets across multiple repositories

**Key Benefits:**

- Consistent code quality across all contributions
- Automatic enforcement without manual intervention
- Configurable based on branch protection needs
- Integration with existing GitHub workflow permissions

For more information, see the [repository rulesets documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

### ⌨️ Activity: Create a repository ruleset

1. In the top navigation, select the **Settings** tab.

1. In the left navigation, expand **Rules** and select **Rulesets**.

1. Click the **New ruleset** button and select the **New branch ruleset** option.

1. Set the ruleset name and status:

   - **Ruleset Name**: `Require Copilot Reviews`
   - **Enforcement Status**: `Active`

1. Under **Target branches**, add protections for the `main` branch.

   1. Click **Add target** and **Include default branch**.
   1. Click **Add target** and **Include by pattern**.
   1. Enter `main` and click the **Add inclusion pattern** button.

   <img width="300" alt="screenshot of target branches" src="https://github.com/user-attachments/assets/217f205c-7a61-4ffa-a0a6-7e76ff8d7906"/>

1. Under **Rules**, enable the following options:

   - **Require a pull request before merging**: ☑️
   - **Require conversation resolution before merging**: ☑️
   - **Automatically request Copilot code review**: ☑️

1. Scroll to the bottom and click the **Create** button.

1. Return to the open pull request.

1. Notice that the merge button is now disabled.

   <img width="300" alt="screenshot of disabled merge button" src="https://github.com/user-attachments/assets/28e4cb05-f09d-423d-8c77-8f0ec61c73ad"/>

1. Click **Resolve conversation** for all current and outdated feedback from Copilot. It is not necessary to implement anything.

1. Merge the pull request.

   > 🪧 **Note**: If the **Merge pull request** button doesn't activate, check for unresolved conversations in the outdated comments.

1. With the pull request merged, wait a moment for Mona to check your work, provide feedback, and provide a final review. Nice work! You are all done! 🎉

### ⌨️ Activity: (optional) Test automatic reviews

Not ready to finish yet? Are you concerned by the hard coded announcement banner? Us too!

So... let's fix it! 🧑‍🚀🚀

> [!NOTE]
> You don't need "fix" the new Announcement feature. If you just want to test automatic reviews, you can just make a quick small change and start a new pull request.

1. In VS Code, switch back to the `main` branch, pull the merged changes, and delete the `add-announcement-banner` branch.

1. Create a new branch from `main` with the following name.

   ```txt
   enable-editing-announcements
   ```

1. Open the Copilot Chat panel and ensure it is in **Agent mode**. Use the following prompt to ask Copilot to upgrade our new Announcements feature.

   > 💡 **Tip**: The premium models (that use PRUs) are typically more robust and will require less, or no, followup prompts for refinement.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > The Announcement feature should not be hard coded.
   >
   > - Make it driven from the database.
   > - Add a button in the header that opens a dialog window. It lists all existing announcements and has controls to add/modify/delete them.
   > - Only signed in users have access to manage announcements.
   > - Announcements require an expiration date. Start date is optional.
   > - Add an example message to the database initialization.
   > - Don't worry about unit testing.
   > - Make it pretty with a good UI/UX experience.
   > ```

1. (optional) Run the application to test the changes and provide followup prompts to Copilot for further refinement.

1. (optional) Before committing the changes, ask for a local review in VS Code.

1. Commit and push the changes.

1. Create a new Pull Request with the following details.

   - **compare:** `enable-editing-announcements`
   - **target:** `main`
   - **title:** `Enable Editing Announcements`

1. Notice that Copilot was automatically added as a reviewer. Wait a moment for feedback.

1. (optional) Address any comments from Copilot.

1. Merge the pull request.

1. Nice work! You are all done, again! 🎉


[x-review.md](https://github.com/user-attachments/files/25344588/x-review.md)
## Review

_Congratulations, you've completed this exercise! You're all set to review lots of contributions from your fellow teachers!_

<img src="https://octodex.github.com/images/jetpacktocat.png" alt=celebrate width=150 align=right>

You've implemented a comprehensive GitHub Copilot code review workflow for the school's extracurricular activities website. Nice work! 🎉

### What you accomplished

In this exercise, you learned how to:

- **Request code reviews from Copilot in VS Code** for immediate feedback on uncommitted changes
- **Assign Copilot as a reviewer on GitHub pull requests** to catch issues before merging
- **Create custom instructions** to tailor review feedback to your team's standards and requirements
- **Implement automatic code reviews** using repository rulesets for consistent quality enforcement

### What's next?

- [Skills: Expand your team with Copilot coding agent](https://github.com/skills/expand-your-team-with-copilot)
- [Skills: Customize your GitHub Copilot Experience](https://github.com/skills/customize-your-github-copilot-experience)
- [Skills: AI in Actions](https://github.com/skills/ai-in-actions)

