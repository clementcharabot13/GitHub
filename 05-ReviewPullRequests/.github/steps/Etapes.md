## Step 1: Open a pull request

_Welcome to "Review pull requests"! :wave:_

Let's get started by opening a **pull request** on some changes that were recently added to the `update-game` branch.

### What is a pull request?

A **pull request** is a collaboration area where work in one branch is reviewed before merging it into another branch. It has different tabs to manage the conversation and easily review changes.

- **Conversation** - A general log of the pull request activity. It also provides an open space for fellow collaborators and the community to provide ideas, suggestions, and general feedback.
- **Commits** - A list of only the commits unique to the proposed branch.
- **Checks** - The results of any automations applied to the pull request using [GitHub Actions](https://github.com/features/actions). That's for another exercise, though. 😎
- **Files Changed** - A [Diff](https://docs.github.com/en/get-started/quickstart/github-glossary#diff) view that easily shows the proposed changes in a before/after view. It also has options to add comments and reviews in context.

> [!TIP]
> You can [create a draft pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) for unfinished work. This can help avoid accidental merges or premature reviews.

### :keyboard: Activity: Create a pull request

1. Open this repository in a new browser tab so you can work on the steps while you read the instructions in this tab.

1. In the top navigation, select the **Pull requests** tab.

1. On the right, click the **New pull request** button.

1. Under the **Compare changes** area, select the following options and click the **Create pull request** button.

   - **base:** `main`
   - **compare:** `update-game`

1. Set the **title** and **description** to the following.

   ```md
   Update game over message
   ```

   ```md
   Update the game over message so people know how to play again!
   ```

1. Click **Create pull request**.

1. With the pull request created, Mona will check your progress and share the next steps.

## Step 2: Assign yourself

_Great job opening that pull request! :wave:_

#### What is an assignee?

A **pull request assignee** is the person (or persons) most familiar with the proposed changes.
It's a simple mechanism for keeping track of who to contact for questions.

### :keyboard: Activity: Assign yourself

1. Navigate back to the created pull request if you are not on it.

1. On the right side, under **Assignees**, click the **assign yourself** text.

1. After assigning yourself, Mona will check your progress and share the next steps.

## Step 3: Leave a review

_You assigned yourself! :tada:_

#### What is a pull request review?

A **pull request review** is feedback from other collaborators or community members on the proposed changes. It helps ensure quality and project momentum. Even more importantly, it's an awesome opportunity to learn more about the project and grow as a developer by seeing how others approach the problem.

Naturally, the best way to get a review is to ask for one. By assigning a reviewer, they get 3 options for providing feedback:

- **Comment** - General feedback without approval or rejection.
- **Approve** - Allows merging if [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), or other policies are enforced.
- **Request Changes** - The proposed changes need do not meet expectations and need additional work. A review should be re-requested after the changes are made.

The **Files changed** tab is the primary place for collecting feedback. It allows for adding comments directly to lines before submitting a review.

### What does a review typically look like?

1. Reviewing the **title** and **description** are clear and concise. It should easily convey the intended changes and any associated issues.

1. Reviewing the **Files changed** tab to ensure all proposed code matches the description.

1. For most updates, try out the proposed change to verify they match the intention.

1. Use the repository's [contributing guide](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors) for any guidance on review requirements, testing, quality verification, etc.

#### Review ideas

- Identify potential issues, risks, and limitations.
- Suggest changes and improvements.
- Share awareness of upcoming changes that the pull request doesn't account for.
- Ask questions to verify shared understanding.
- Highlight what the author did well and what they should keep doing.
- Prioritize the most important feedback.
- Be concise _and_ provide meaningful detail.
- Treat the pull request author with kindness and empathy.

### :keyboard: Activity: Leave a review

1. On the pull request, click the **Files changed** tab.

1. Take a moment to review the change.

   - Notice the change is a simple wording adjustment.

1. Above the comparison view, click the **Review changes** button.

1. Enter the following comment and click the **Submit review** button.

   ```md
   Looks good to me. I think this is more intuitive. Nice work!
   ```

   > 🪧 **Note:** You can't choose **Approve** or **Request changes** on your own pull request.

1. With your review submitted, Mona will check your progress and share the next steps.

## Step 4: Suggest changes

_Nice work reviewing that pull request :sparkles:_

While reviewing, it is very common to find simple changes that are easier to implement than to describe. For example, typos or rewording sentences. These are perfect situations for the **Add a suggestion** feature.

### How do I suggest a change?

The **Add a suggestion** feature is a button in the comment text editor. It inserts a specially formatted code block. Instead of only showing a comment, GitHub will also provide a **Commit changes** button. This allows the author to accept the suggestion and commit it with the push of a button. No need to open a code editor! Nice!

### :keyboard: Activity: Suggest changes

1. On the pull request, click **Files changed**.

1. Find the comparison view for the `index.html` file.

1. Hover your cursor next to the line numbers for the modified line.

1. Click the plus icon to show an inline comment form.

1. Click the **Add a suggestion** button to insert a modifiable copy of the line.

   <img width="300" alt="add-a-suggestion-button" src="https://github.com/clementcharabot13/05-ReviewPullRequests/blob/main/.github/images/add-a-suggestion-button.png?raw=true" />

1. Edit the suggestion to match below and click the **Add a single comment** button.

   ````md
   ```suggestion
   <h2 hidden>Game over! Want to play again?! Just click refresh. 🧑‍🚀!</h2>
   ```
   Let's make it a bit more friendly. 🤓
   ````

### :keyboard: Activity: Apply a suggested change

1. Click the **Commit suggestion** button to open a commit message form.

1. Edit the commit message to the below text and click the **Commit changes** button.

   ```markdown
   Make the end game experience more friendly
   ```

1. With the changes committed, Mona will check your progress and share the next steps.

## Step 6: Merge your pull request

_Almost done!_ :heart:

With our reviews collected and feedback implemented, it's time to merge the changes.

### :keyboard: Activity: Merge your pull request

1. In the pull request navigation, select the **Conversation** tab.

1. Scroll down and click the **Merge pull request** button.

1. (Optional) Delete the `update-game` branch.

1. With the pull request merged, Mona will check your progress and prepare a final review. Congrats, you are done! 🎉

## Review

_Congratulations friend, you've completed this course!_

<img src=https://octodex.github.com/images/hula_loop_octodex03.gif alt=celebrate width=300 align=right>

As you continue working on GitHub, remember that high quality reviews improve your projects. If you are new to a repository, inquire about what review practices they have so you can hit the ground running.

Here's a recap of all the tasks you've accomplished in your repository:

- You learned how to assign pull requests for review.
- You left a review on a pull request.
- You suggested changes to a pull request.
- You applied suggested changes to a pull request.

### What's next?

- Try adding a [`CODEOWNERS`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) file to your project to automatically assign reviewers to pull requests.
- [Take another GitHub Skills exercise](https://skills.github.com).
- [Read the GitHub Getting Started docs](https://docs.github.com/en/get-started).
- To find projects to contribute to, check out [GitHub Explore](https://github.com/explore).
