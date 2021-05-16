---
title: "Using GitHub for Team Collaboration"
date: 2019-4-27
last_modified_at: 2021-1-17
tags: [git, github, tutorial]
excerpt: "Tutorial on how to use Git and GitHub for team collaboration on a project. Content includes installing, setting up, creating a repository, making commits, undoing stuffs, creating branches, merging branches etc."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/github_desktop_webview.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: techniques
---

{% include toc %}

## Why do we use Git?
<p>Git can record changes to our file over time. We can recall any specific version of the file at any given time. It also allows many people to easily collaborate on a project and have their own version of the project files on their local computer. It is incredibly useful to keep all the histories of the project codes so that if we want to go back the previous version in the future, we don’t need to rewrite it but we can just switch back to the past version directly.</p>

## What is GitHub?
<p>Okay! So far we understood git to some extent. But what is “GitHub”? Well, GitHub is an online service that hosts our projects, helpful in sharing our code to other collaborators of the project. The collaborators can simply download the codes and work on them. They can re-upload their edits and merge with the main codebase.</p>

{% include google-adsense-inarticle.html %}

## Git
### Installing Git
<p>The easiest way is just to download from the link <a href="https://git-scm.com/downloads">here</a>. Select the download for your operating system and this will download in your computer. Go through the installation steps and that’s it, you have Git now! If you are Windows user, then I’d suggest you install some text editor for writing and running codes. My personal favorite is “VSCode” by Microsoft. It is free, open-source and cross-platform i.e. it provides a similar environment for Windows, Linux, and Mac Users and it has inbuilt “terminal”.</p>
<p>After installing Git and supposedly VSCode then you open and terminal and type</p>
<p><code>git --version</code></p>


### Setting up Git
<p>Now, after installing Git in your local computer, the first thing that you wanna do is to set it up so that Git could know you. We can tell Git about us by telling the username and email.</p>
<pre><code>git config --global user.name utpalkumar
git config --global user.email utpalkumar50@gmail.com</code></pre>
<p>&nbsp;</p>

### How Git works?
<p>We make a container for our project where we dump all our codes and it is popularly called repositories (or repo, for short). We can have a repository on our local computer as well as remotely on some kind of online repository hosting service like GitHub. We can track the contents of the repository using Git. Git tracks the history of the contents of the repository using the so-called “commits”. Commits are the different points in the history of making the repository where we have told the Git to save. We tell the Git to save the version using the “commit” command which we will see in detail later. If we have made, say 5 commits to our repository, we can roll back to any previous commit smoothly.</p>

### Creating a repository
<p>We first open an editor and a terminal for typing the commands. In VSCode, we can do it both in one window.</p>

<p>Make sure the terminal and the editor points to the same path.</p>
- To initialize empty Git repository in the directory, we type in the terminal:

<p><code>git init</code></p>

<p>The existence of the .git directory in our working directory shows that this is now the git repository. We can even initialize Git in a directory which already has contents in the same way.</p>
<p>After initializing the Git in the working directory, we can create and modify any files in the current directory or the sub-directory. After finishing the code modification, we can check the status of the Git using the command</p>

{% include google-adsense-inarticle.html %}

<p><code>git status</code></p>
<p>It will show the status of files which are tracked and untracked. We can add all the files in the current directory and subsequent subdirectory for the tracking using the command:</p>
<p><code>git add .</code></p>
<p>Alternatively, we can also add each file separately by their names.</p>

<p>Sometimes, we don’t wanna add some files for committing to track using the Git but by mistake, it gets added. To remove those files, we can use the command:</p>
<p><code>git rm --cached filename</code></p>
<p>If we modify the file “testApp.py” and then run the command</p>
<p><code>git status</code></p>


### Making Commits
<p>In simple words, a commit is a safe-point, a snapshot in time of our code at a particular point.</p>
<p><code>git commit -m "some message"</code></p>

<p>Please make sure to add meaningful messages to the commits so that at some point if we wanna go back to the previous version, we can figure that out easily using the message.</p>

<p>If we wanna see the history of all our commits we can use the command</p>
<p><code>git log</code></p>

{% include google-adsense-inarticle.html %}

<p>Sometimes, if we have a lot of commits, we don’t wanna print everything out. So, we can condense the output of the log using the command:</p>
<p><code>git log --oneline</code></p>


### Undoing stuff
<p>Undoing the mistake of one version is the primary goal of using Git. Let’s see how we can execute that. We can rewind the commit and go back to the previous version. We can do that by three ways in the order of increasing risk:</p>
<ol start="1">
<li>Checkout commit: Very safe option. Best option to go back to the past version without getting rid of any other versions.</li>
<li>Revert commit: Apparently, delete some unrequired commits from the history.</li>
<li>Reset commit: We need to be very sure before we do this. This will permanently delete all the commits after the point we move to.</li>
</ol>



<p>Here, I have added 2 more commits and output the total of 4 commits.</p>
<p>Now, if we wanna see the state of the code at the point we added the axis labels only, we can do that.</p>
<p><code>git checkout 016b638</code></p>

<p>This takes us back immediately to the previous version where we didn’t have the title or have changed the line styles. This is the best way to go back in time, inspect the past without changing anything. Now, we can come back to the present time by just using the command:</p>
<p><code>git checkout master</code></p>

<p>&nbsp;</p>
<p>Now, let’s say we wanna remove the commit where we have added the title to the plot. We can do that using the command:</p>
<p><code>git revert 60c62cb</code></p>
<p>When we execute this command, we get the following on the screen. Don’t get intimidated. This is a vim text editor which is asking you to give the title to this commit.</p>

<p>We type “:wq” to save that file and quit.</p>

<p>Now, we can see that this has removed the line in the code which added the title to the plot. But when we log the commits, we see that it has not actually deleted the commit but added a new commit which has reverted that commit.</p>
<p>Okay, if we want to permanently delete some commits and go back to the point in history, we can use the “reset” option</p>
<p><code>git reset 016b638</code></p>

<p>Now, we see that all the commits from the point we moved in the past has been deleted but the code stays unchanged. This is a good way to merge some commits into one. But if we are really strict and want to change the code as well, we can do that using the flag “hard”:</p>

<p>Beware that now there is no way to get back to the versions where we had title and linestyles.</p>

### Branches
<p>So far we have been working on one branch that is the “master” branch of the repository. When we make any commits, we were committing only to the master branch. We usually use the master branch to represent the stable version of our codes. For that reason, we don’t really wanna try new features or new codes on this branch as there is a risk of messing up the code. What we can do is try out the new feature in an isolated environment and if we like it then we can merge then in the master branch. This is mainly useful if more than one person is working on a project. They can make the branch of the code, apply several new features and when they are really satisfied then they can add it to the master branch.</p>

<p>If we wanna add the branch at this point of the code, we can do</p>

{% include google-adsense-inarticle.html %}

<p><code>git branch feature1</code></p>
<p>If we wanna see all the branches, we type</p>
<p><code>git branch -a</code></p>

<p>The asterisk (*) in front of “master” shows that we are currently on the master branch. To switch the branch, we use</p>
<p><code>git checkout feature1</code></p>

<p>Now, we can work on the branch “feature1” separately than the master branch</p>

<p>When we switch back to the master branch, we can notice that we have not actually added any title</p>

<p>If the things don’t work out as expected, we can even delete the branch</p>
<p><code>git checkout master</code># first we move to the master branch</p>
<p><code>git branch -d feature1</code> # this will give the error because this branch has not been merged with the master branch</p>
<p>Instead, we can use</p>
<p><code>git branch -D feature1</code></p>
<p>to forcibly delete the branch.</p>
<p>Okay, now let&#8217;s see more about working with the branches. The quick way of making a branch and checkout to it is</p>
<p><code>git checkout -b feature-a</code></p>
<p>Now, we work on this branch.</p>

<p>Now, we have two branches “feature1” and “feature-a” going on at the same time. But neither one is affecting the original codes. One branch has some changes to the plotting of the data and the other branch is having the title to the plot. Now, how do we merge those two changes to the master branch?</p>

### Merging Branches
<p>To merge the branches, we first need to move to the branch into which we wanna merge, which in our case is master branch.</p>
<p><code>git checkout master</code></p>
<p><code>git merge feature1</code></p>

<p>Now, let’s merge the other branch</p>

<p>This time, we encounter some conflicts to the merge. In this case, we need to manually fix the conflict and then add the files using</p>
<pre><code>git add .
git commit
</code></pre>

        

## GitHub
<p>We first need an account on the GitHub. You can sign up on <a href="https://github.com/">the GitHub website</a>.


### Pushing code to Github
Now, we push the code from our master branch to the GitHub
<pre><code>git status
git push https://github.com/utpalrai/learn_git.git master
</code></pre>

<p>Now, let&rsquo;s add some more changes to the master branch and push those changes to the GitHub. Before that, we can create an alias to the long address to the online repository of the GitHub so that we don&rsquo;t need to type that again and again. Here, we use &ldquo;origin&rdquo; as an alias.<br />
<code>git remote add origin https://github.com/utpalrai/learn_git.git</code> Now, we can simply type <code>git push origin master</code>to push the repository to the remote location on GitHub.</p>

<p>Cloning remote repository locally</p>
<p>We can instead do the other way round too. We can clone the online repository onto our local computer.</p>


### Collaborating on GitHub
<p>The first thing we should make sure that we have the updated master code present locally. We can pull the code using the pull command in the cloned directory <code>git pull origin master</code> Now, we made a new branch called complex_app and made some changes and commit those changes.</p>
 

<p>Now, we want to push this branch to the remote repository on the GitHub. We do not want to merge this with the master and then push to the remote GitHub repository as this will mess up the master branch on the GitHub. Later, all the collaborators can review the code and then decide if they wanna merge it or not.</p>


### Forking
<p>We can fork the repo on GitHub in order to contribute to some open source project. The forking will copy the open source project from other&rsquo;s account to our own account. After that, we can clone that repository to our local computer. Later if we wanna contribute to that project, we can do the pull request. And then if the original creator of the project accepts the pull request then they can merge it to the original project.</p>

{% include google-adsense-inarticle.html %}
        
## Github Desktop
Recently, Github released [Github Desktop](https://desktop.github.com/), which is a GUI app for visualizing and managing repositories and branches, linking your local filesystem with your GitHub account. It is available for both Windows and Mac (Alas! not for linux yet but you can use [Sublime Merge}(https://www.sublimemerge.com/) alternatively). This makes the task of collaboration even easier. I strongly recommend the use of GitHub Desktop.


<p align="center">
    <a href="https://desktop.github.com/" style="text-decoration: none;"><img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/github_desktop_webview.png"></a>
  </p>
  