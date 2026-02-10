## Step 1: Create a branch

_Welcome to "Introduction to GitHub"! :wave:_

**What is GitHub?**: GitHub is a collaboration platform that uses _[Git](https://docs.github.com/get-started/quickstart/github-glossary#git)_ for versioning.
GitHub is a popular place to share and contribute to [open-source](https://docs.github.com/get-started/quickstart/github-glossary#open-source) software.

:tv: [Video: What is GitHub?](https://www.youtube.com/watch?v=pBy1zgt0XPc)

**What is a repository?**: A _[repository](https://docs.github.com/get-started/quickstart/github-glossary#repository)_ is a project containing files and folders.
A repository tracks versions of files and folders. For more information, see
"[About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)" from GitHub Docs.

**What is a branch?**: A _[branch](https://docs.github.com/en/get-started/quickstart/github-glossary#branch)_ is a parallel version of your repository.
By default, your repository has one branch named `main` and it is considered to be the definitive branch.
Creating additional branches allows you to copy the `main` branch of your repository and safely make any changes without disrupting the main project.
Many people use branches to work on specific features without affecting any other parts of the project.

Branches allow you to separate your work from the `main` branch.
In other words, everyone's work is safe while you contribute.
For more information, see "[About branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)".

**What is a profile README?**: A _[profile README](https://docs.github.com/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)_
is essentially an "About me" section on your GitHub profile where you can share information about yourself with the community on GitHub.com.
GitHub shows your profile README at the top of your profile page. For more information, see "[Managing your profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)".

![screenshot showing an example profile readme](https://github.com/user-attachments/assets/fdc3a590-0bab-4758-9aec-6fd93c1d81a6)

### :keyboard: Activity: Your first branch

1. Open a new browser tab and navigate to your newly made repository (your copy of this exercise). Then, work on the steps in your second tab while you read the instructions in this tab.

2. Navigate to the **< > Code** tab in the header menu of your repository.

   ![screenshot highlighting the code tab](https://github.com/user-attachments/assets/9a310b11-d80b-4b0f-bddc-aa41a8c01269)

3. Click on the **main** branch drop-down.

   <img width="300" alt="screenshot highlighting the branch selection" src="https://github.com/user-attachments/assets/9256e36d-4c17-4629-95df-863d42a3c182">

4. In the text box **Find or create a branch...**, enter `my-first-branch`.
   
   > **Note:** This is checked to continue with the next step. :wink: 

5. Click the text **Create branch: `my-first-branch` from main** to create your branch.

   <img width="300" alt="screenshot highlighting the create branch prompt" src="https://github.com/user-attachments/assets/df0f369f-0669-4f9e-b9f3-b82515ec2a6c">

   - The branch will automatically switch to the one you just created.
   - The **main** branch drop-down menu will display your new branch name.

6. Now that your branch is pushed to GitHub, Mona should already be busy checking your work. Give her a moment and keep watch in the comments. You will see her respond with progress info and the next lesson.


<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:
- Make sure your created the branch with the exact name `my-first-branch`. No prefixes or suffixes.

</details>

## Step 2: Commit a file

_You created a branch! :tada:_

Creating a branch allows you to edit your project without changing the `main` branch. Now that you have a branch, it’s time to create a file and make your first commit!

**What is a commit?**: A _[commit](https://docs.github.com/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits)_ is a set of changes to the files and folders in your project. A commit exists in a branch. For more information, see "[About commits](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits)".

### :keyboard: Activity: Your first commit

The following steps will guide you through the process of committing a change on GitHub. A commit records changes to the project such as adding/removing/renaming files and modifying file content. For this exercise, committing a change will be adding a new file to your new branch.

> [!NOTE]
> `.md` is a file extension that creates a Markdown file. You can learn more about Markdown by visiting "[Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)" in our docs or by taking the "[Communicating using Markdown](https://github.com/skills/communicate-using-markdown)" Skills Exercise.

1. On the **< > Code** tab in the header menu of your repository, make sure you're on your new branch `my-first-branch`.

2. Select the **Add file** drop-down and click **Create new file**.

   <img width="300" alt="screenshot of the create new file option" src="https://github.com/user-attachments/assets/a86c088e-b377-43f7-96e6-e68f7aef1cd3">

3. In the **Name your file...** field, enter `PROFILE.md`.

4. In the **Enter file contents here** area, copy the following content to your file:

   ```
   Welcome to my GitHub profile!
   ```

   ![screenshot for adding the profile.md file](https://github.com/user-attachments/assets/487c0ba4-88d8-4634-8715-a170413369d0)

5. Click **Commit changes...** in the upper right corner above the contents box. A dialog will appear.

6. GitHub offers a simple default message, but let's change it slightly for practice. Enter `Add PROFILE.md` in the **Commit message** field.
   
   - A **commit message** and optional **extended description** help provide clarity for your changes. This is particularly useful when your commit involves several files.

   <img width="400" alt="screenshot of adding a new file with a commit message" src="https://github.com/user-attachments/assets/5472be49-6a6c-4b9c-ba2b-151ded73921f">

6. In this lesson, we'll ignore the other fields for now and click **Commit changes**.

7. Now that you've changed a file, Mona should already be busy checking your work. Give her a moment and keep watch in the comments. You will see her respond with progress info and the next lesson.


<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:
- Make sure you are on the `my-first-branch` branch.
- Ensure the `PROFILE.md` file is created and in the root folder.

</details>

## Step 3: Open a pull request

_Nice work making that commit! :sparkles:_

Now that you have made a change to the project and created a commit, it’s time to share your proposed change through a pull request!

**What is a pull request?**: Collaboration happens on a _[pull request](https://docs.github.com/en/get-started/quickstart/github-glossary#pull-request)_. The pull request shows the changes in your branch to other people and allows people to accept, reject, or suggest additional changes to your branch. In a side by side comparison, this pull request is going to keep the changes you just made on your branch and propose applying them to the `main` project branch. For more information about pull requests, see "[About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)".

### :keyboard: Activity: Create a pull request

You may have noticed after your commit that a message displayed indicating your recent push to your branch and providing a button that says **Compare & pull request**.

![screenshot of message and button](https://github.com/user-attachments/assets/a9f29bd2-0461-4bf9-9935-67730761bcd3)

To create a pull request automatically, click **Compare & pull request** button, and then skip to step 5 below. Alternately, you practice creating it manually using the first 4 steps.

1. In the header menu of your repository, click the **Pull requests** tab .
2. Click the **New pull request** button.
3. Select the following branches using the dropdown menus.
   
   - **base:** `main`
   - **compare:** `my-first-branch`

   ![screenshot showing both branch selections](https://github.com/user-attachments/assets/8f01524c-c973-4f4f-a75c-0717fe09b664)

4. Click **Create pull request**.

5. Enter a title for your pull request. By default, the title will automatically be the name of your branch. For this exercise, let's edit the field to say `Add my first file`.

6. The next field helps you provide a **description** of the changes you made. Please enter a short description of what you’ve accomplished so far. As a reminder, you have: created a new branch, created a file, and made a commit.

   ![screenshot showing pull request](https://github.com/user-attachments/assets/c6e6af6b-d31e-4628-91ac-de6adb5b390c)

7. Click **Create pull request**.

8. Now that you've started a place to collaborate, Mona should already be busy checking your work. Give her a moment and keep watch in the comments. You will see her respond with progress info and the next lesson.


<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:
- Make sure your pull request title is correct.
- Ensure your pull request has a description.

</details>

## Step 4: Merge your pull request

_Nicely done! :sunglasses:_

You successfully created a pull request. Now it's time to merge it!

**What is a merge?**: A _[merge](https://docs.github.com/en/get-started/quickstart/github-glossary#merge)_ adds the changes in your pull request and branch into the `main` branch. For more information about merges, see "[Merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request)."

![screenshot of green merge pull request button](https://github.com/user-attachments/assets/c691b064-0bd3-4448-bdcd-b1ad82fc9154)

### :keyboard: Activity: Merge the pull request

1. Click **Merge pull request**.

   > **Note:** You may see workflows running on your new pull request, causing the merge button to be inactive. Just wait a moment for them to finish and the merge button will activate.

2. Click **Confirm merge**.

   > **Tip:** Did you notice this dialog looks similar to adding a file? A merge is also a kind of commit!

3. Once your branch has been merged, you don't need it anymore. To delete this branch, click **Delete branch**.

   ![screenshot showing delete branch button](https://github.com/user-attachments/assets/29ddff73-865b-485c-abc6-3333bca71b76)

4. Now that your work is merged, Mona will confirm and share some final review content. Nice work! 🎉

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:
- Make sure you completed the previous lessons. If they haven't passed, the merge button will be gray.

</details>

## Review

_Congratulations, you've completed this Exercise and joined the world of developers!_

<img src=https://octodex.github.com/images/collabocats.jpg alt=celebrate width=300 align=right>

Here's a recap of your accomplishments:

- You learned about GitHub, repositories, branches, commits, and pull requests.
- You created a branch, a commit, and a pull request.
- You merged a pull request.
- You made your first contribution! :tada:

### What's next?

If you'd like to make a profile README, use the quickstart instructions below or follow the instructions in the [Managing your profile README](https://docs.github.com/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme) article.

1. Make a new public repository with a name that matches your GitHub username.
2. Create a file named `README.md` in its root. The "root" means not inside any folder in your repository.
3. Edit the contents of the `README.md` file.
4. If you created a new branch for your file, open and merge a pull request on your branch.
5. Lastly, we'd love to hear what you thought of this exercise [in our discussion board](https://github.com/orgs/skills/discussions/categories/introduction-to-github).

Check out these resources to learn more or get involved:

- Are you a student? Check out the [Student Developer Pack](https://education.github.com/pack).
- [Take another GitHub Skills exercise](https://learn.github.com/skills).
- [Read the GitHub Getting Started docs](https://docs.github.com/en/get-started).
- To find projects to contribute to, check out [GitHub Explore](https://github.com/explore).
