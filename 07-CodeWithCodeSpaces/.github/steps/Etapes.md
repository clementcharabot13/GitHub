## Step 2: Use a custom image in your codespace

The didn't specify any configuration for the codespace we just created, so GitHub used a default Docker image. While this is very useful, it won't be consistent and it doesn't version lock our runtime environment. Specifying the configuration is important to keep the development environment repeatable.

Let's do that now by providing a specific docker container image.

### How to configure a Codespace?

Configuration is provided directly in the repository via the `.devcontainer/devcontainer.json`. You can even add multiple configurations!

Let's create this file and set a few of the most common settings. For other options like setting configuring VS Code, forwarding ports, and running lifecycle scripts, see the [Codespaces documentation](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces) on GitHub.

### ⌨️ Activity: Customize the codespace

1. Ensure you are in the VS Code Codespace.

1. Use the VS Code file explorer to create the configuration file.

   ```txt
   .devcontainer/devcontainer.json
   ```

   Alternately, run the below terminal command to create it.

   ```bash
   mkdir -p .devcontainer
   touch .devcontainer/devcontainer.json
   ```

1. Open the `.devcontainer/devcontainer.json` file and add the following content. Let's start with a basic image.

   ```json
   {
     "name": "Basic Dev Environment",
     "image": "mcr.microsoft.com/vscode/devcontainers/base:debian"
   }
   ```

   > 💡 **Tip**: The name is optional but it will help identify the configuration when creating a codespace on GitHub, if there are multiple options.

1. After saving, VS Code likely popped up a notification that it detected a configuration change. You can **Accept** that option to rebuild the development container or manually use the Command Palette (`CTRL`+`Shift`+`P`) and run the command `Codespaces: Rebuild Container`. Select the **Rebuild** option. A full build is not necessary.

   <img width="350" alt="rebuild codespace command" src="https://github.com/user-attachments/assets/2b72e1a7-68c4-4c8d-8bf1-5727a520fd0e"/>

1. Wait a few minutes for the Codespace to rebuild and VS Code to reconnect.

1. Expand the lower panel and select the **TERMINAL** tab.

1. Use the following command to check the tool versions again. Notice that none are installed now!

   ```bash
   node --version
   dotnet --version
   python --version
   gh --version
   ```

1. ⚠️ There is currently a bug with Codespaces that expects [Git-LFS](https://git-lfs.com/) to be installed. Run the following command to remove the affected Git hooks.

   ```bash
   rm .git/hooks/post-checkout
   rm .git/hooks/post-commit
   rm .git/hooks/post-merge
   rm .git/hooks/pre-push
   ```

1. With our new configuration verified, let's commit the changes. Use VS Code's source control tools or the below terminal command.

   ```bash
   git add '.devcontainer/devcontainer.json'
   git commit -m 'feat: Add codespace configuration'
   git push
   ```

1. With our dev container configuration committed, Mona will begin checking your work. Give her a moment to provide feedback and the next learning steps.

## Step 3: Add Features

You can further customize your codespace by adding container feature, VS Code extensions, VS Code settings, host requirements, and much more.

Let's add the GitHub CLI, extensions to run the python program using VS Code, and a custom script to install some packages when first creating the Codespace.

### ⌨️ Activity: Add support for the Python

1. In VS Code, open the Command Palette (`CTRL`+`SHIFT`+`P`) and select the below command.

   ```txt
   Codespaces: Add Dev Container Configuration Files...
   ```

   <img width="350" alt="vs code configure dev container command" src="https://github.com/user-attachments/assets/38265419-47bf-4ac8-a0fd-71ea67e2d6eb" />

1. Select the option `Modify your active configuration...`.

1. In the list of features, search for and select `Python` from `devcontainers`.

   - Instead of the defaults, pick `Configure Options`.
   - Leave `Install Tools` set to `true`.
   - Select Python version: `3.10`

1. Navigate to and open the `.devcontainer/devcontainer.json` file.

1. Verify a new entry similar to the below was added.

   ```json
   "features": {
      "ghcr.io/devcontainers/features/python:1": {
         "installTools": true,
         "version": "3.10"
      }
   },
   ```

### ⌨️ Activity: Add VS Code extensions

1. In the left navigation, select the **Extension** tab.

   <img width="200" alt="vs code extensions tab" src="https://github.com/user-attachments/assets/d7941711-e5a9-4871-83f3-c723c203bc70" />

1. Search for `python` and find entries for `Python` and `Python Debugger`.

   <img width="250" alt="python extensions for vs code" src="https://github.com/user-attachments/assets/b34ef808-2023-41f2-8963-85ba04d5684b" />

1. Right click on each entry and select the `Add to devcontainer.json` option.

   <img width="250" alt="add to devcontainer config button" src="https://github.com/user-attachments/assets/30ada390-c8a7-4175-9d83-dfa17fc83de3" />

1. Navigate to and open the `.devcontainer/devcontainer.json` file.

1. Verify a new entry similar to the below was added.

   ```json
   "customizations": {
      "vscode": {
         "extensions": [
            "ms-python.python",
            "ms-python.debugpy"
         ]
      }
   },
   ```

### ⌨️ Activity: Add a custom script

The Dev Container specification provides multiple locations to run [lifecycle scripts](https://containers.dev/implementors/json_reference/#lifecycle-scripts) to further customize your Codespace. Let's add the `postCreateCommand` which runs one time after initial build (or rebuild).

1. Use the VS Code file explorer to create a script file with the below name.

   ```txt
   .devcontainer/postCreate.sh
   ```

   Alternately, run the below terminal command to create it.

   ```bash
   touch .devcontainer/postCreate.sh
   ```

1. Make the script executable by running the below terminal command.

   ```bash
   chmod +x .devcontainer/postCreate.sh
   ```

1. Open the `.devcontainer/postCreate.sh` file and add the following code, which will install an animation of a steam locomotive.

   ```bash
   #!/bin/bash

   sudo apt-get update
   sudo apt-get install sl
   echo "export PATH=\$PATH:/usr/games" >> ~/.bashrc
   echo "export PATH=\$PATH:/usr/games" >> ~/.zshrc
   ```

1. Navigate to and open the `.devcontainer/devcontainer.json` file.

1. Create the `postCreateCommand` entry at the same level (_top level_) as `features`, and `customizations`.

   ```json
   "postCreateCommand": ".devcontainer/postCreate.sh"
   ```

1. With our new configuration finished, let's commit the changes. Use VS Code's source control tools or the below terminal command.

   ```shell
   git add '.devcontainer/devcontainer.json'
   git add '.devcontainer/postCreate.sh'
   git commit -m 'feat: Add features, extensions, and postCreate script'
   git push
   ```

1. Open the VS Code Command Palette (`CTRL`+`Shift`+`P`) and run the `Codespaces: Rebuild Container` command. Select the **Rebuild** option. A full build is not necessary.

   <img width="350" alt="rebuild codespace command" src="https://github.com/user-attachments/assets/2b72e1a7-68c4-4c8d-8bf1-5727a520fd0e"/>

1. Wait a few minutes for the Codespace to rebuild and VS Code to reconnect.

1. With the customizations committed, Mona will begin checking your work. Give her a moment to provide feedback and the next learning steps.

> [!TIP]
> You can also configure your account to [install dotfiles](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account), allowing you to combine personal configurations with the project's configuration.

### ⌨️ Activity: (optional) Verify our customizations

Now that you've rebuilt the codespace, let's verify the python extension, python version, and custom script were adjusted correctly in the Codespace.

1. Ensure you are in the Codespace.

1. In the left sidebar, click the extensions tab and verify that the Python extensions are installed and enabled.

   <img width="250" alt="python extensions for vs code" src="https://github.com/user-attachments/assets/b34ef808-2023-41f2-8963-85ba04d5684b" />

1. In the left sidebar, select **Run and Debug** tab and then press the **Start Debugging** icon. VS Code will open the lower panel and show the run logs.

   <img width="250" alt="run and debug tab pointing to start button" src="https://github.com/user-attachments/assets/63327b56-b033-4ca1-aa83-93ec076389f5"/>

1. In the lower panel, switch to the **TERMINAL** tab.

1. Run the following command to show the installed version of Python. Notice the others are not installed.

   ```bash
   node --version
   dotnet --version
   python --version
   gh --version
   ```

1. Run the following command to show the steam locomotive animation.

   ```bash
   sl
   ```

## Step 4: Test out our Codespace

The final test of our Codespace is to put ourselves in the position of an onboarding developer. Let's close everything and start up a new Codespace from nothing.

### ⌨️ Activity: Delete the existing codespace

1. Close the window running your VS Code Codespace.

1. Navigate to your exercise repository.

1. Above the files list on the right, click the green **<> Code** button.

1. Select the **Codespaces** tab to show the list of created Codespaces.

   <img width="250" alt="list of codespaces" src="https://github.com/user-attachments/assets/2ed90b91-0c62-4c49-96f5-75abbb34a989" />

1. Find the active entry, select the three dot menu `...`, and select the **Delete** command.

   <img width="500" alt="delete codespace command" src="https://github.com/user-attachments/assets/911a62a5-c50f-497b-a853-6e3865886211" />

> [!TIP]
> You can manage all of your Codespaces across all projects at https://github.com/codespaces

### ⌨️ Activity: Start a codespace

1. Above the files list on the right, click the green **<> Code** button.

1. Select the **Codespaces** tab and click the **plus sign** `+` or **Create codespace on main** button.

   > Alternately you can select the three dot menu `...` to choose a different machine type, location, or configuration.

1. Wait a few minutes for the Codespace to be created and VS Code to connect.

1. (optional) Test out some of the activities from the previous steps to see if they still work!

1. Add an issue comment to let Mona know you finished this activity, then give her a moment to share the final review.

   ```md
   Hey @professortocat, I've finished testing out my new Codespace.
   I'm ready to review!
   ```

1. Nice work! You are all done! 🎉

## Review

<img src="https://octodex.github.com/images/welcometocat.png" alt=celebrate width=300 align=right>

Here's a recap of all the tasks you've accomplished in your repository:

- You learned how to create a codespace and push code to your repository from the codespace.
- You learned how to use custom images, features, extensions, and scripts in your codespace.
- You learned how to test run it like an onboarding developer.

### Additional learning and resources

- [Developing in a codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/developing-in-a-codespace). Learn how to delete a codespace, open an existing codespace, connect to a private network, forward ports, and much more.
- [Set up your repository](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers). Learn how to set minimum machine specs for a codespace, add badges, set up a template repo, and much more.
- [Personalize and customize GitHub Codespaces](https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-github-codespaces-for-your-account). Learn how to use setting sync for your codespace, add dotfiles, set the default region, set the default editor, and much more.
- [Prebuild your codespace](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds)
- [Manage your codespace](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-github-codespaces-for-your-organization)

### What's next?

- [Take another GitHub Skill exercise](https://github.com/skills).
- [Read the Get started with GitHub docs](https://docs.github.com/en/get-started).
- To find projects to contribute to, check out [GitHub Explore](https://github.com/explore).

## Step 1: Start a codespace and push some code

### What's the big deal about Codespaces?

A **codespace** is a development environment hosted in the cloud, defined by configuration files in your repository. This creates a repeatable development environment tailored specifically to the project that simplifies developer onboarding and avoids the famous phrase "It works on my machine!" 😎

Each codespace follows the [Dev Container specification](https://containers.dev/implementors/spec/) and is hosted by GitHub as a [Docker container](https://code.visualstudio.com/docs/devcontainers/containers).

But don't worry! You don't need to know Docker or even have it installed on your machine!

> [!TIP]
> Since the Dev Container configuration is part of the repository, you can also use it locally with your own Docker host. Nice!

A Codespace has several advantages/features compared to local development. To name a few:

- Start a codespace directly from the repository page.
- Develop in the browser. No IDE installation required.
  - Option to use a local install of VS Code to link to the remote Codespace.
- Preconfigure everything you need to run the project:
  - Add **[features](https://containers.dev/features)** to install common development needs.
  - Run scripts at various steps of the codespace lifecycle _(e.g install python/npm packages)_.
  - Setup VS Code settings and extensions to match the project needs.
- Fast internet access (since the container is in the datacenter).

> [!TIP]
> Codespaces are even useful in short-lived situations like reviewing a pull request. No need to verify you have the right setup to test out the incoming code changes.

Let's get started! We'll start up a Codespace, run the application, make a change, and push it. Like normal development! 🤓

### ⌨️ Activity: Start a codespace

1. Open a second tab and navigate to this repository. Ensure you are on the **Code** tab.

1. Above the files list on the right, click the green **<> Code** button.

   <img width="300" alt="green code button" src="https://github.com/user-attachments/assets/a9d80b0d-4614-4b26-83dd-b4b6fefd76c9" />

1. Select the **Codespaces** tab and click the **Create codespace on main** button. A new window will open running VS Code and it will connect to the remote Codespace. Wait a few minutes for the codespace to be created.

1. Look in the bottom left of the VS Code window see the remote connection.

   <img width="350" alt="remote connection status in VS Code" src="https://github.com/user-attachments/assets/35fa3230-db51-4a9d-a82b-3a1184e2e9a0"/>

> [!TIP]
> GitHub uses the [universal](https://github.com/devcontainers/images/tree/main/src/universal) Codespace image if the repository doesn't include a configuration. It includes several useful and commonly used tools.

### ⌨️ Activity: Run the application

1. Ensure you are in the VS Code Codespace.

1. In the left sidebar, select the file **Explorer** tab and open the file `src/hello.py`.

   <img width="250" alt="vs code explorer tab" src="https://github.com/user-attachments/assets/76af1f05-1fed-43ff-b362-43d1c6c6cc53" />

1. In the lower panel, select the **TERMINAL** tab.

   <img width="350" alt="vs code terminal tab" src="https://github.com/user-attachments/assets/9bb493b6-167c-4414-8f39-ab9c4baa5514" />

1. Paste the following command in the Codespace's remote terminal to show the installed versions of several tools. Note the versions for comparison later.

   ```bash
   node --version
   dotnet --version
   python --version
   gh --version
   ```

1. Paste the following command to run the Python program in the Codespace's remote terminal.

   ```bash
   python src/hello.py
   ```

### ⌨️ Activity: Push changes to your repository from the codespace

1. Replace the `src/hello.py` file contents with the following and save the file.

   ```py
   print("Hello World!")
   ```

1. With the message updated, commit the change and push it to GitHub. Use VS Code's source control tools or the below terminal commands.

   ```bash
   git add 'src/hello.py'
   git commit -m 'fix: incomplete hello message'
   git push
   ```

1. (optional) Back in your web browser, open the `src/hello.py` file to to verify the change was updated.

1. With the the change pushed to GitHub, Mona will begin checking your work. Give her a moment to provide feedback and the next learning steps.
