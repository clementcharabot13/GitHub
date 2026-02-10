## Step 1: Enable GitHub Pages

### 📖 Theory: What is GitHub Pages?

GitHub Pages lets you turn your repository into a website. This is a great way to share your project, resume, portfolio, documentation, or even a blog with the world.

When you enable GitHub Pages on a repository, GitHub takes the content that's on the main branch and publishes a website based on its contents.

> [!NOTE]
> Learn more in the [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages).

### ⌨️ Activity: Enable GitHub Pages



1. Open this repository in a new browser tab so you can work on the steps while you read the instructions in this tab.
1. Under your repository name, click **Settings**.
1. Click **Pages** in the **Code and automation** section.
1. Ensure **Deploy from a branch** is selected from the **Source** drop-down menu, and then select `main` from the **Branch** drop-down menu.
1. Click the **Save** button.

1. With GitHub Pages enabled Mona will be preparing the next step in this exercise!


<details>
<summary>Having trouble? 🤷</summary><br/>

- Turning on GitHub Pages creates a deployment of your repository. GitHub Actions may take up to a minute to respond while waiting for the deployment. Future steps will be about 20 seconds; this step is slower.

</details>

## Step 2: Customize your homepage

Good job! You turned on GitHub Pages! :tada:

You can see the link to your website at the top of the [Pages](https://github.com/{{full_repo_name}}/settings/pages) section of your repository settings _(you may need to refresh it)_

> [!TIP]
> Keep your GitHub Pages [website](https://{{login}}.github.io/{{repo_name}}/) open in a separate browser tab and keep it handy!
>
> As you progress through this exercise, you'll see your changes reflected on your live site.

### 📖 Theory: Customizing your homepage

You can customize your homepage by adding content to  `index.md` file. As you commit it to the `main` branch your website will be updated to display your personalized content!

### ⌨️ Activity: Create your homepage

1. Browse to the `index.md` file in the `main` branch.
1. In the upper right corner, open the file editor.
1. Type the content you want on your homepage. You can use Markdown formatting on this page.
1. (optional) You can also modify `title:` or leave it as it is.
1. Commit your changes to the `main` branch.
1. As you commit your changes Mona will prepare the next step in this exercise!


<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure you are editing the `index.md` file in the `main` branch.

</details>

## Step 3: Configure your site

Nice work updating your home page :sparkles:

It's time we give it a little bit of **configuration** so it looks nice!

### 📖 Theory: Jekyll and \_config.yml

Jekyll uses a file titled `_config.yml` to store settings for your site, your theme, and reusable content like your site title and GitHub handle. Learn more in the [Jekyll configuration documentation](https://jekyllrb.com/docs/configuration/).

For this activity, we will use a blog-ready theme named "minima".

### ⌨️ Activity: Configure your site

1. Browse to the `_config.yml` file in the `main` branch.
1. In the upper right corner, open the file editor.
1. Add a `theme:` set to **minima** so it shows in the `_config.yml` file as below:

   ```yml
   theme: minima
   ```

1. (optional) You can modify the other configuration variables such as `title:`, `author:`, and `description:` to further customize your site.

   <details>
   <summary>Example </summary><br/>

   ```yml
   theme: minima
   title: {{ login }}'s personal blog
   description: This is where I share cool stuff about my life
   author: {{ login }}
   ```

   </details>

1. Commit your changes to the `main` branch.
1. As you commit your changes Mona will prepare the next step in this exercise!


<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure you are editing the `_config.yml` file in the `main` branch`.
- Double-check your YAML formatting. Indentation and colons matter!

</details>

## Step 4: Create a blog post

Your home page is looking great! :cowboy_hat_face:

### 📖 Theory: Jekyll blog posts and frontmatter



Jekyll uses specially named files and frontmatter to create blog posts. The files must be named `_posts/YYYY-MM-DD-title.md` and must include `title` and `date` in the **front matter**.

**Front matter** is a yaml section at the **top** of your file that looks like this:

```yaml
---
title: "Welcome to my blog"
date: 2025-05-15
---
```

> [!NOTE]
> Learn more in the [Jekyll frontmatter documentation](https://jekyllrb.com/docs/front-matter/).


### ⌨️ Activity: Create a blog post

1. Browse to the `main` branch.
1. Click the `Add file` dropdown menu and then on `Create new file`.
1. Name the file following the `_posts/YYYY-MM-DD-title.md` format.
1. Replace the `YYYY-MM-DD` with today's date, and change the `title` of your first blog post if you'd like.
   > If you do edit the title, make sure there are hyphens (-) between your words.
   > If your blog post date doesn't follow the correct date convention, you'll receive an error and your site won't build. For more information, see "[Page build failed: Invalid post date](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/troubleshooting-jekyll-build-errors-for-github-pages-sites)".
1. Type the following content at the top of your blog post:

   ```yaml
   ---
   title: "YOUR-TITLE"
   date: YYYY-MM-DD
   ---
   ```

   1. Replace `YOUR-TITLE` with the title for your blog post.
   1. Replace `YYYY-MM-DD` with today's date.
1. Type a quick draft of your blog post. Remember, you can always edit it later.
1. Commit your changes to the `main` branch.
1. As you commit your changes Mona will prepare the next step in this exercise!

<details>
<summary>Having trouble? 🤷</summary><br/>

- Double-check your file name and date format.
- Make sure your frontmatter is at the very top of the file and formatted correctly.

</details>

## Review

_Congratulations, you've completed this exercise and learned a lot about GitHub Pages and Jekyll!_

<img src="https://octodex.github.com/images/constructocat2.jpg" alt="celebrate" width=300 align=right>

Here's a recap of your accomplishments:

- You enabled GitHub Pages.
- You selected a theme using the config file.
- You learned about proper directory format and file naming conventions in Jekyll.
- You created your first blog post with Jekyll and GitHub Pages!

### What's next?

- Keep working on your GitHub Pages site... we love seeing what you come up with!
- [Take another GitHub Skills exercise](https://learn.github.com/skills).
- [Read the GitHub Pages docs](https://docs.github.com/en/pages).
