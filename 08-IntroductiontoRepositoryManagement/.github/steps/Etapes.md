# Step 2: Prepare to collaborate

Your simple school website has become quite popular! After showing it at the last staff meeting, Ms. Rodriguez from the Art Club and Mr. Chen from the Chess Club came up to you super excited. They have tons of ideas for new features!

- Ms. Rodriguez wants to add a photo gallery
- Mr. Chen dreams of adding a tournament bracket system for the chess/sports activities! 🎨♟️

While you're thrilled about their enthusiasm, you realize you need to set up some guidelines before letting them start changing code. The last thing you want is conflicting changes breaking the registration system right before spring break!

Opening your project to other teachers at Mergington High means thinking about how everyone will collaborate together without breaking each other's code.

**Collaborators** are the people you have granted write access to the project through repository settings.

- Provide other people permissions to change project files while still protecting repository settings.
- Personal repositories have simple permissions. Organization repositories allow flexible permissions such as read, write, maintain, and admin.

To help with collaboration, GitHub provides two special files:

1. **`CONTRIBUTING.md` file** - A "How to Help" guide. Some example content:

   - How to prepare a developer setup of the extra-curricular activities website.
   - The process for suggesting changes.
   - The project's coding style preference, to keep things consistent.
   - How to ask for help when stuck.

1. **`CODEOWNERS` file** - Assign specific people or teams responsible for a portion of the project.

   - When someone creates a pull request, GitHub will automatically ask the right person to review it.

## ⌨️ Activity: Create a welcoming contribution guide

The IT Club meeting is tomorrow, and you need to prepare for Ms. Rodriguez and Mr. Chen to join the project. Let's start a document to help them contribute effectively.

1. At the top navigation, return to the **Code** tab. Ensure you are on the `prepare-to-collaborate` branch.

   <img width="350" alt="image showing the correct branch" src="https://github.com/user-attachments/assets/68cd1e7a-1b34-47eb-9f0b-095d47442b12" />

1. In the top directory, create a new file called `CONTRIBUTING.md` (case sensitive).

1. Add a welcoming message.

   ```md
   # Contributing to the Mergington High Extra-Curricular Activities Website

   Thank you for your interest in helping improve our school's website!
   Whether you want to add your club's activities, fix a bug, or suggest
   new features, this guide will help you get started. 🎉
   ```

1. Add instructions to help teachers quickly start developing.

   ```md
   ## Development Setup

   1. Clone the repository to your computer.
   2. Install Python requirements: `pip install -r requirements.txt`.
   3. Run the development server: `python src/app.py`.
   4. Visit http://localhost:8000 in your browser to see the website.

   ## Making Changes

   1. Create a new branch for your changes.
      - Use descriptive names like `art-gallery-feature` or `fix-chess-signup`
   2. Make your changes and test them locally with sample student data.
      - Use the MongoDB extension to preview the included sample date.
   3. Push your branch and create a pull request.
   4. Wait for review and address any feedback.

   ## Code Style

   - Follow PEP 8 for Python code (backend).
   - Use clear, descriptive variable names (student_name, start_time, etc.)
   - Add comments to describe blocks of logic.
   ```

1. Add a section for getting help.

   ```md
   ## Need help or have ideas?

   - Check the open issues first.
     - If your problem is there, add a comment or up-vote.
     - If not there, create a new issue. Be as descriptive as possible.
   - Ask in our weekly IT Club office hours (Thursdays at lunch in Room 203).
   - For other general problems, email the tech team at techclub@mergingtonhigh.example.edu
   ```

1. In the top right, use the **Commit changes...** button and commit your changes directly to `prepare-to-collaborate` branch.

## ⌨️ Activity: Assign code ownership

With others joining the fun, you want to stay involved on anything affecting architecture and core functionality. Let's assign you to the related files.

1. At the top navigation, return to the **Code** tab. Ensure you are on the `prepare-to-collaborate` branch.

1. In the top directory, create a new file called `CODEOWNERS` (case sensitive and no extension).

1. Add the following content:

   ```codeowners
   # Core functionality - changes here should be rare!
   /src/app.py                   @{{ login }}
   /src/backend/database.py      @{{ login }}
   /src/backend/routers/auth.py  @{{ login }}

   # The frontend will need refactored soon to be more object oriented.
   /src/static/   @{{ login }}
   ```

1. In the top right, use the **Commit changes...** button and commit your changes directly to `prepare-to-collaborate` branch.

1. With the files committed, wait a moment for Mona to check your work, provide feedback, and share the next lesson.

## ⌨️ Activity: (Optional) Add your first collaborator

Ready to let your colleague start working on that photo gallery feature? Let's do it!

> [!IMPORTANT]
> This step is optional because it requires another person with a GitHub account to participate.

1. In the top navigation, select the **Settings** tab.

1. In the left navigation, select **Collaborators**.

1. Find the **Manage access** area and click the **Add people** button.

   <img width="350" alt="" src="https://github.com/user-attachments/assets/686c32c6-11c2-4e69-bad1-39062d5b4376" />

1. Enter a friend/colleague's GitHub username or email then press the **Add to repository** button.

   <img width="350" alt="" src="https://github.com/user-attachments/assets/d0eaf344-baf0-4a9c-9291-c11e7a9fdaa3" />

> [!IMPORTANT]
> Personal repositories only have one collaboration role type. A "collaborator" receives **write** permissions but NOT **admin** permissions. If you need finer permissions, consider starting a free [organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations) and assigning [repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).

# Step 3: Foster healthy growth

With so many eager contributors, Principal Martinez pulled you aside after morning announcements: "Your website is becoming critical school infrastructure! We need to make sure it grows in a healthy way as more teachers join. Can you add some guidelines to keep everything organized?"

As your extra-curricular activities website grows, you'll need more than just technical protections and contribution guides. You'll also have to encourage healthy and constructive communication.

Let's look at a couple ways to do that:

1. **Code of Conduct** - This document sets expectations for how community members should interact. Think of it like the Student Handbook at Mergington High - it outlines respectful behavior, how to report non-technical problems, and consequences for violations.

2. **Issue Templates** - These provide structure when someone reports a problem or suggests a new feature. They can help the community effectively communicate their needs for new features and provide enough information to solve bugs.

## ⌨️ Activity: Set expectations with a Code of Conduct

Let's start by establishing some community guidelines for your growing team of teacher-contributors.

> [!TIP]
> The [Contributor Covenant](https://www.contributor-covenant.org/) is a popular code of conduct used by many projects.

1. At the top navigation, return to the **Code** tab. Ensure you are on the `prepare-to-collaborate` branch.

1. In the top directory, create a new file called `CODE_OF_CONDUCT.md` (case sensitive).

1. Add the following content:

   ```markdown
   # Mergington High School Code of Conduct

   ## Our Pledge

   In the interest of fostering an open and welcoming environment for
   our school community, we as contributors and maintainers pledge to
   make participation in the Extra-Curricular Activities project a
   respectful and harassment-free experience for everyone.

   ## Our Standards

   Examples of behavior that contributes to creating a positive environment include:

   - Using welcoming and inclusive language
   - Being respectful of differing viewpoints and experiences
   - Gracefully accepting constructive criticism
   - Focusing on what is best for the students and the school community
   - Showing empathy towards other community members

   Examples of unacceptable behavior include:

   - The use of inappropriate language or imagery
   - Trolling, insulting comments, and personal attacks
   - Public or private harassment
   - Publishing others' private information without explicit permission
   - Other conduct which could reasonably be considered inappropriate in a school setting

   ## Responsibilities

   Project maintainers are responsible for clarifying the standards of
   acceptable behavior and are expected to take appropriate and fair
   corrective action in response to any instances of unacceptable behavior.

   Project maintainers have the right and responsibility to remove, edit,
   or reject comments, commits, code, issues, and other contributions that
   are not aligned to this Code of Conduct.

   ## Scope

   This Code of Conduct applies both within project spaces and in public spaces
   when an individual is representing the project or the school. Examples of
   representing the project include using an official project email address,
   posting via an official social media account, or acting as an appointed
   representative at an online or offline event.

   ## Enforcement

   Instances of abusive, harassing, or otherwise unacceptable behavior may be
   reported to the IT Club faculty advisor. All complaints will be reviewed and
   investigated promptly and fairly.

   Project maintainers who do not follow or enforce the Code of Conduct in good faith may
   face temporary or permanent repercussions as determined by the school administration.

   ## Attribution

   This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org),
   version 1.4, available at [https://www.contributor-covenant.org/version/1/4/code-of-conduct.html](https://www.contributor-covenant.org/version/1/4/code-of-conduct.html)
   ```

1. In the top right, use the **Commit changes...** button and commit your changes directly to `prepare-to-collaborate` branch.

## ⌨️ Activity: Communicate easier with issue templates

Now let's create templates so other teachers can report bugs or request features in a standardized way.

> [!TIP]
> You might consider trying the public preview for [issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms), which provide a friendlier user experience when creating issues.

1. In the top navigation, select the **Settings** tab.

1. Find the **Features** section and verify **Issues** is enabled.

   <img width="350" alt="" src="https://github.com/user-attachments/assets/dafb976b-4b8c-4c5e-8989-04d3e7bbe70d" />

1. Click the **Set up templates** button to enter the issue templates editor.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/bd94af1e-d564-472f-a435-f12fa1bf3b5c" />

1. Click the **Add template** dropdown and select **Bug report**.

   <img width="350" alt="" src="https://github.com/user-attachments/assets/baee263d-b233-4029-b629-9544eacf1e27" />

1. Click the **Preview and edit** button to show the current template. Click the **Edit icon** (pencil) to make the fields editable.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/1c8500f7-10b2-406b-9385-d5b9480e2f71" /><br/>

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/77e312e2-af3c-4015-94f0-b1cf7409cc40" /><br/>

   <img width="700" alt="image" src="https://github.com/user-attachments/assets/c2aecd6e-d021-4149-b088-7cbf883a7e33" />

1. (Optional) Let's keep it simple for our students and fellow teachers. Remove the sections about Desktop and Smartphone details.

1. Repeat the above steps for the "Feature request" template.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/6456e261-fcd8-4845-b1ab-f2c2d5883c77" />

1. With our templates prepared, let's commit them. In the top right, click the **Propose changes** button. Enter a description and set the branch to `add-issue-templates`, then click **Commit changes**. You can ignore the automatically created pull request.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/a00a3740-ce0c-430c-9541-e56b7d9b45d6" />

1. With the files committed, wait a moment for Mona to check your work, provide feedback, and share the next lesson.

> [!TIP]
> Did you notice that you are working in parallel on 2 branches now? That's exactly what working with multiple collaborators is like.

# Step 4: Prepare for the inevitable

As you settle into the teachers' lounge with your coffee, you realize something: With more and more teachers contributing to the code, it's only a matter of time before security vulnerabilities creep in. 😱

Every codebase, no matter how well-maintained, will eventually face security challenges. Let's try to proactively prepare for that day by configuring a few tools GitHub offers:

1. **Dependabot** - Track and create alerts for vulnerabilities found in upstream dependencies used in your project. Automatically create pull requests to upgrade dependencies to safe versions.

1. **Code Scanning** - Analyze your repository's code to find security vulnerabilities and coding errors. Use GitHub Copilot Autofix to automatically suggest fixes for these alerts.

1. **Security Policy and Private vulnerability reporting** - Provide a guide and simple form for security researchers and end users to responsibly report vulnerabilities directly to the repository maintainer. This prevents sensitive issues from being publicly disclosed before they're fixed.

> [!NOTE]
> This is just a quick setup guide. For a more detailed setup of each service, we recommend the related GitHub Skills exercises and/or GitHub documentation.

## ⌨️ Activity: Automate security updates with Dependabot

Let's configure Dependabot to use default settings and automatically combine fixes for open alerts, and create pull requests. This will allow us to stay up to date with very little overhead! Nice!

> [!TIP]
> For a deeper dive, check out the [Secure Repository Supply Chain](https://github.com/skills/secure-repository-supply-chain) Skills exercise!

1. In the top navigation, select the **Settings** tab.

1. In the left navigation, select **Advanced Security**.

1. Find the **Dependabot** section. Verify or change the settings to match the following:

   - **Dependabot alerts**: `enabled`
   - **Dependabot security updates**: `enabled`
   - **Grouped security updates**: `enabled`

1. Find **Dependabot version updates** and click the **Enable** button. This will open an editor to create a configuration file.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/a4d7ae19-0439-4b78-bcbf-9fce5c5410ff" />

1. In the left files list, at the top, click the **Expand file tree** button to show the list of files. At the top, change the branch to `prepare-to-collaborate`. Remember, our ruleset won't let us directly change files on `main`.

   <img width="500" alt="image" src="https://github.com/user-attachments/assets/18a3cd1a-75ab-4e5e-a4c4-efd175d91ced" />

1. Set the `package-ecosytem` to `pip` so Dependabot will automatically monitor our Python requirements.

   <img width="500" alt="image" src="https://github.com/user-attachments/assets/0bc90e67-4b71-4780-8272-20dc0fff5c4c" />

1. In the top right, use the **Commit changes...** button and commit your changes directly to `prepare-to-collaborate` branch.

## ⌨️ Activity: Detect dangerous patterns with code scanning

None of us at the high school are professional software developers. Let's enable code scanning to alert us if we are potentially doing something unsafe. And, let's configure GitHub Copilot to create pull requests with solutions.

> [!TIP]
> Want to learn more about code scanning and writing custom queries? Check out the [Introduction to CodeQL](https://github.com/skills/introduction-to-codeql) Skills exercise after you finish this one!

1. In the top navigation, select the **Settings** tab.

1. In the left navigation, select **Advanced Security**.

1. Find the **Code scanning** section. Click the **Set up** button and select the **Default** option to open a configuration panel.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/5b3a89e5-c71a-44d9-b917-d1a21dc52181" />

1. Click the **Enable CodeQL** button to accept the default configuration.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/6d5f7164-d8ed-4b5d-bbcf-8aed9e7acc5d" />

1. Below the **Tools** section. Verify **Copilot Autofix** is set to `On`.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/b9d57e7a-f392-4c51-b137-f205a77adb79" />

## ⌨️ Activity: Provide a safe path for security findings

Now that the automated options are ready, let's create a guide for real-life humans to report any security vulnerabilities they find in a safe way.

1. In the top navigation, select the **Settings** tab.

1. In the left navigation, select **Advanced Security**.

1. Find the **Private vulnerability reporting** setting and verify it is `enabled`.

1. At the top navigation, click the **Security** tab.

1. In the left navigation, click the **Policy** option.

1. Click the **Start setup** button. An editor will be started to create the file `SECURITY.md`.

   <img width="350" alt="" src="https://github.com/user-attachments/assets/183b9fcc-1521-47fd-8165-b476a8ccb370"/><br/>

   <img width="350" alt="" src="https://github.com/user-attachments/assets/36c272d1-bc4a-48c8-b234-56173a214cdb"/>

1. In the left files list, at the top, click the **Expand file tree** button to show the list of files. At the top, change the branch to `prepare-to-collaborate`. Remember, our ruleset won't let us directly change files on `main`.

1. We will ignore the provided template and instead use a recommendation from Mergington High School's IT department. Add the following content:

   > 💡**Tip** If you switch to a branch that does not contain the same file, the editor will become empty. Press the **Restore** button to retrieve the previous editor's content.

   ```markdown
   # Mergington High School Security Policy

   ## Reporting a Vulnerability

   At Mergington High, we take the security of our Extra-Curricular Activities website seriously, especially
   since it contains student information. If you discover a security vulnerability, please follow these steps:

   1. **Do not** create an issue on this repository, disclose the vulnerability publicly, or discuss it with other teachers/students.
   1. In the top navigation of this repository, click the **Security** tab.
   1. In the top right, click the **Report a vulnerability** button.
   1. Fill out the provided form. It will request information like:
      - A description of the vulnerability
      - Steps to reproduce the issue
      - Potential impact on student data or website functionality
      - Suggested fix (if you have one)
   1. Email the IT Club faculty advisor at techsupport@mergingtonhigh.example.edu and inform them you have made a report. **Do not** include any vulnerability details.

   ## Response Timeline

   - We will acknowledge receipt of your report within 2 school days
   - We will provide an initial assessment within 5 school days
   - Critical issues affecting student data will be addressed immediately
   - We will create a private fork to solve the issue and invite you as a collaborator so you can see our progress and contribute.

   ## Thank You

   Your help in keeping our school's digital resources secure is greatly appreciated!
   Responsible disclosure of security vulnerabilities helps protect our entire school community.
   ```

1. In the top right, use the **Commit changes...** button and commit your changes directly to `prepare-to-collaborate` branch.

1. With the files committed, wait a moment for Mona to check your work, provide feedback, and share the next lesson.

# Step 5: Release

With all our preparations ready, it's time to release them!

## ⌨️ Activity: Merge our collaboration changes

1. In the top navigation, select the **Pull requests** tab.

1. Find the pull request for the `prepare-to-collaborate` branch and merge it. You may need to wait for your new security scans to finish.

1. Find the pull request for the `add-issue-templates` branch and merge it. You may need to wait for your new security scans to finish.

1. With both pull requests merged, Mona will prepare the final review and acknowledge the exercise as finished! Nice work! You are all done! 🎉

## Review

_Congratulations, you've completed this exercise! You're all set for an awesome time collaborating with your fellow teachers!_

<img src="https://octodex.github.com/images/jetpacktocat.png" alt=celebrate width=150 align=right>

You've successfully prepared Mergington High's extracurricular activities website for healthy and safe collaboration. Make sure you let the principal know so he can brag to the IT department about your proactive efforts!

Here is a snippet of something you can share:

- Protected our code from accidental mistakes with `.gitignore` and branch protections.
- Set clear guidelines for teacher contributions with `CONTRIBUTING.md` and `CODEOWNERS`.
- Established community standards with a Code of Conduct and structured issue templates.
- Prepared for the future security challenges by enabling automated scanning and providing safe submission procedures.

### What's next?

This exercise was meant to introduce you to many of the different areas of managing a repository. However, there is still more to learn!

Here are some additional exercises for a deeper dive:

- [Skills: Secure your repository supply chain](https://github.com/skills/secure-repository-supply-chain)
- [Skills: Introduction to CodeQL](https://github.com/skills/introduction-to-codeql)
- [Skills: Introduction to Secret Scanning](https://github.com/skills/introduction-to-secret-scanning)

Here are some useful references from the [GitHub Docs](https://docs.github.com/en):

- [How to ignore files](https://docs.github.com/en/get-started/git-basics/ignoring-files)
- [Template gitignore files](https://github.com/github/gitignore)
- [Creating rulesets for a repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#using-fnmatch-syntax)
- [Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule)
- [About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [Setting guidelines for contributors](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [Add a code of conduct](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project)
- [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)
- [Adding a security policy](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)

# Step 1: Protect your code

It's been a busy month at Mergington High! Your simple website for managing extra-curricular activities has really taken off. What started as a basic sign-up form for a few activities has grown into the go-to place for half the school activities. 📚✨

Principal Martinez was so impressed with your work that they announced at the last staff meeting that ALL clubs should start using the website. While this is exciting, you're a bit nervous - the last thing you want is an accidental change breaking the system right before the big Fall Activities Fair! 😰

When more teachers start helping with the Mergington High activities website, it's important to add some safeguards. Thankfully, GitHub provides several ways to protect your repository:

1. **Repository Rulesets** - These provide safeguards to limit:

   - Pushing code directly to important branches
   - Deleting or renaming branches
   - Force pushing (which can overwrite history)
   - (and much more)

1. **`.gitignore`** - This special file tells Git which files it should NOT track, like:

   - Temporary files that your code creates while running
   - Secret configuration files with sensitive information
   - System files that other developers don't need

> [!TIP]
> Think of these settings like the editorial process of a school yearbook. Various student committees will take photos and write articles, then the yearbook president will make adjustments to make sure everything flows together properly. Finally, a teacher/advisor will sign off that all content is appropriate.

## ⌨️ Activity: (optional) Get to know our extracurricular activities site

<details>
<summary>Show Steps</summary>

In [Getting Started with GitHub Copilot](https://github.com/skills/getting-started-with-github-copilot/) exercise, we have been developing the Extracurricular activities website. You can follow these steps to start up the development environment and try it out.

> ❗ **Important:** Opening a development environment and running the application is **NOT** necessary to complete this exercise. You can skip this activity if desired.

1. Right-click the below button to open the **Create Codespace** page in a new tab. Use the default configuration.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Wait some time for the environment to be prepared. It will automatically install all requirements and services.

1. Validate the **GitHub Copilot** and **Python** extensions are installed and enabled.

   <img width="300" alt="copilot extension for VS Code" src="https://github.com/user-attachments/assets/ef1ef984-17fc-4b20-a9a6-65a866def468" /><br/>
   <img width="300" alt="python extension for VS Code" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />

1. Try running the application. In the left sidebar, select the **Run and Debug** tab and then press the **Start Debugging** icon.

   <details>
   <summary>📸 Show screenshot</summary><br/>

   <img width="300" alt="run and debug" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />

   </details>

   <details>
   <summary>🤷 Having trouble?</summary><br/>

   If the **Run and Debug** area is empty, try reloading VS Code: Open the command palette (`Ctrl`+`Shift`+`P`) and search for `Developer: Reload Window`.

   <img width="300" alt="empty run and debug panel" src="https://github.com/user-attachments/assets/0dbf1407-3a97-401a-a630-f462697082d6" />

   </details>

1. Use the **Ports** tab to find the webpage address, open it, and verify it is running.

   <details>
   <summary>📸 Show screenshot</summary><br/>

   <img width="350" alt="ports tab" src="https://github.com/user-attachments/assets/8d24d6b5-202d-4109-8174-2f0d1e4d8d44" />

   ![Screenshot of Mergington High School WebApp](https://github.com/user-attachments/assets/5e1e7c1e-1b0e-4378-a5af-a266763e6544)

   </details>

</details>

## ⌨️ Activity: Add a branch ruleset

To get started, let's add some protections so that no one accidentally breaks the club registration system.

1. If necessary, open another tab and navigate to this repository. We will start on the **Settings** tab.

1. In the left navigation, expand the **Rules** area and select **Rulesets**.

1. Click the **New ruleset** dropdown and select **New branch ruleset**.

   <img width="250" alt="image" src="https://github.com/user-attachments/assets/1e9fd519-1421-4d6b-b654-a3fe53a8fb75" />

1. Set the **Ruleset Name** as `Protect main` and change the **Enforcement status** to `Active`.

   <img width="250" alt="image" src="https://github.com/user-attachments/assets/ce30fd34-39b5-4e22-b348-4af61fd05cd1" />

1. Find the **Targets** section and use the **Add target** dropdown to add 2 entries:

   1. Add the **Include default branch** option to ensure protections aren't bypassed by switching the default branch.

      <img width="250" alt="image" src="https://github.com/user-attachments/assets/217263cc-d5c2-4ac0-b03c-a72494e5c812" />

   1. Use the **include by pattern** option and enter the pattern `main`.

      <img width="250" alt="image" src="https://github.com/user-attachments/assets/968c9ed8-b051-44eb-af42-d99670ad31fd" />

      <img width="250" alt="image" src="https://github.com/user-attachments/assets/ddc52767-d93e-4c9e-a77a-90c3b5c08fb5" />

1. Find the **Rules** section and ensure the following items are checked.

   - [x] Restrict deletions
   - [x] Require a pull request before merging
     - Required approvals: `0`
     - [x] Require review from Code Owners
   - [x] Block force pushes

1. Scroll to the bottom and click the **Create** button to save the ruleset.

## ⌨️ Activity: Create a `.gitignore` file

We know many teachers use different tools, so let's make sure they don't accidentally commit unnecessary files.

1. At the top navigation, return to the **Code** tab and verify you are on the `main` branch.

1. Above the list of files, click the **Add file** dropdown and select **Create new file**.

   <img width="300" alt="New file button" src="https://github.com/user-attachments/assets/8f3f8da8-1471-485a-9df5-8c03ecba2d8e"/>

1. Enter the file name `.gitignore`. We will ignore the template selector for now and make our own. Copy the below example content into it.

   <img width="350" alt="preview of new file" src="https://github.com/user-attachments/assets/580d1a63-a264-4d44-8901-50ad708b8822"/>

   ```gitignore
   # Python backend for club management
   __pycache__/
   *.py[cod]      # Python compiled files
   *$py.class
   *.so
   .Python
   env/
   .env           # Where database passwords are stored
   venv/          # Virtual environment for testing
   .venv

   # Teacher IDE settings
   .vscode/       # Ms. Rodriguez uses VS Code
   .idea/         # Mr. Chen uses PyCharm

   # Local development & testing
   instance/
   .pytest_cache/
   .coverage      # Test coverage reports
   htmlcov/

   # Staff computer files
   .DS_Store      # For teachers with Macs
   Thumbs.db      # For teachers with Windows
   ```

1. In the top right, select the **Commit changes...** button. Notice that it won't let us commit to the `main` branch! Our ruleset is working! Nice!

   <img width="400" alt="image" src="https://github.com/user-attachments/assets/4e85948d-75c8-4c13-8ddd-4707bf9b0805" />

1. Enter `prepare-to-collaborate` for the branch name then click the **Propose changes** button. You will be forwarded to a new page to start a new pull request.

1. Set the title to `Prepare to collaborate` and click the **Create pull request** button. **Do NOT merge yet**, since we will be adding more collaboration related changes.

1. With the file committed, wait a moment for Mona to check your work, provide feedback, and share the next lesson.

> [!TIP]
> GitHub and the community have built a repository with [sample `.gitignore` files](https://github.com/github/gitignore) for many situations. Make sure to check it out!

<details>
<summary>🤷 Having trouble?</summary><br/>

Make sure you pushed the `.gitignore` file to `prepare-to-collaborate` branch. Exact naming for both matters!

</details>
