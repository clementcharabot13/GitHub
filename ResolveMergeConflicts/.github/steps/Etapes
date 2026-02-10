## Step 1: Learn about merge conflicts

### What is a merge conflict?

A **merge conflict** occurs when changes are made to the same part of the same file on two different branches.

```mermaid
gitGraph
    checkout main
    commit id: "Initial"
    commit id: "Add resume.md"

    branch my-resume
    checkout my-resume
    commit id: "Update skills"

    checkout main
    commit id: "Also update skills"

    checkout my-resume
    commit id: "Other changes"

    checkout main
    merge my-resume id: "Conflict!"
```

**What's happening here:**

1. We start with a repository and add a `resume.md` file.
2. We create a new branch called `my-resume` and update the skills area.
3. At the same time, someone else also updates the skills area on the `main` branch.
4. We add other unrelated changes to the `my-resume` branch.
5. When we try to merge `my-resume` into `main`, we get a **conflict!** Both branches modified the same part of `resume.md`.

### ⌨️ Activity: Create a pull request

To quickly practice, we already created the above scenario for you by making a new branch `my-resume` then modifying `resume.md` on both branches, which will will cause a conflict. Let's practice with it!

1. Open this repo in a new browser tab, and work on the steps in your second tab while you read the instructions in this tab.

1. In the top navigation, select the **Pull requests** tab.

1. Click the **New pull request** button and use the following settings:

   - Base: `main`
   - Compare: `my-resume`
   - Title: `Resolve a merge conflict`

1. With the new pull request opened, Mona will share the next steps.

## Step 2: Resolve a merge conflict

Managing conflicts can be intimidating, but have no fear, Git is smart with merging! Git only needs a human to decide when the situation is very unclear.

You typically have 3 options for managing a conflict:

1. Accept the version from the base branch.
1. Accept the version from the compare branch.
1. Manually combined the changes from both branches.

> [!TIP]
> You can learn more about managing conflicts on the [GitHub Docs: resolve the conflict](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line) page.

### When should I resolve a conflict?

Conflicts can be resolved as soon as they are noticed. Resolving a conflict doesn't automatically merge the pull request in GitHub. Instead, it stores the conflict's resolution as a **reverse merge** commit, allowing you to keep working on your branch as normal.

This means that some changes from the `base` branch (`main`) are merged into the `compare` branch (`my-resume`). Only the `compare` branch is updated, which allows you to test the resolved changes before merging.

```mermaid
gitGraph
    checkout main
    commit id: "Initial"
    commit id: "Add resume.md"

    branch my-resume
    checkout my-resume
    commit id: "Update skills"

    checkout main
    commit id: "Also update skills"

    checkout my-resume
    commit id: "Other changes"

    checkout my-resume
    merge main id: "Resolve conflict"
    commit id: "Continue work"

    checkout main
    merge my-resume id: "Success!"

```

### ⌨️ Activity: Resolve a merge conflict

1. If needed, open the recently created pull request.

1. Scroll to the bottom of the page. Near the merge button, notice a message indicating there are conflicts to be resolved.

1. Press the **Resolve conflicts** button to open a special text editor for handling merge conflicts.

1. Look for a highlighted section similar to the below, which shows both versions of the conflict.

   ```txt
   <<<<<<< my-resume
   - Contributed to open source projects
   =======
   - Built internal tools
   >>>>>>> main
   ```

1. After some inspection, we decide to keep the version from the compare branch. Remove the base branch version by deleting then content between `=======` and `>>>>>>> main`.

   ```txt
   <<<<<<< my-resume
   - Contributed to open source projects
   =======
   >>>>>>> main
   ```

1. With our manual changes finished, let's remove the merge conflict markers. Only the content from the compare branch will remain.

   ```txt
   - Contributed to open source projects
   ```

1. In the top right, click the **Mark as resolved** button and choose **Commit merge**.

1. With the conflict resolved, Mona will share the next steps.

## Step 3: Merge your pull request

Nice work! All that remains is to merge!
Yep, that's it! Merge conflicts can be easy! 🥰

### ⌨️ Activity: Merge your pull request

1. Click the **Merge pull request** button.

1. (optional) Delete the branch `my-resume`.

1. With the pull request merged, Mona will share a final review then update the readme to share your success. Nice work! 😎

## Review

<img src=https://octodex.github.com/images/benevocats.jpg alt=celebrate width=300 align=right>

Congratulations! You've successfully completed the **Resolve Merge Conflicts** exercise. 🎉

You've learned essential skills for collaborative development on GitHub:

- **Understanding merge conflicts**: You now know why conflicts occur when multiple people edit the same file
- **Identifying conflicts**: You can recognize when GitHub detects merge conflicts in pull requests
- **Resolving conflicts**: You've practiced using GitHub's web editor to manually resolve conflicts by choosing which changes to keep
- **Merging successfully**: You completed the workflow by merging your pull request after resolving conflicts

### What's next?

Check out other [GitHub Skills exercises](https://learn.github.com/skills).

- [GitHub Pages](https://github.com/skills/github-pages) - Publish your own static website for free.
- [Communicate using Markdown](https://github.com/skills/communicate-using-markdown) - Improve your documentation skills
- [Getting Started with GitHub Copilot](https://github.com/skills/getting-started-with-github-copilot) - Learn, build, debug and ship faster with an AI pair programmer.
