# GPT-4O-AUDIO-PREVIEW - 4 - 05-inferred-corrections

**Audio:** 4.mp3
**Prompt:** 05-inferred-corrections
**Model:** gpt-4o-audio-preview

---

Okay, so some editing instructions for my personal website. 

For the projects homepage, which is kind of important because I like to share what I'm working on, I wanted "MyWordPrompts" as the podcast that I've been planning for a while. I didn’t want "flagship project" to be actually written, and purple looks kind of off. 

And "projects" kind of encompasses both tech repositories as well as publishing efforts. For example, "MyWordPrompts" is—I would say we can have a section here called "Content." There’s a bit of overlap with the content dropdown, but it can be this project. "AI-generated podcast" can actually be described as, and it’s not "3000+ prompts"; that’s a different project completely. This one is just AI-generated podcast: I provide prompts, they get read in the form of an AI response, and that gets combined into one episode. That’s the concept of it. 

The projects homepage is important because I want to just have a place where I show the stuff that I’m working on without getting swamped in all the details, because there’s a lot of stuff that I’ve been adding to the site. 

Maybe we can have dropdown elements within development, data, research—and I think there’s actually more to it than that. I’m just looking under projects. If I click on "by category," the main ones: evaluations and experiments are something I’m very interested in. Also lists—resource lists is how we refer to them, so I think that could be "Claude," "code" definitely, and "MCP." Those would be the big ones—and voice and speech tools. Those are the big ones where I’d say my main areas of focus in AI are. On the projects I’m working on, those would be the top levels I’d like to highlight here. So I think that data is a good one to have, but that would be a better organization and then maybe linking off to those category pages. 

And some of the question is really, what’s the hierarchy here? Those ones I defined are kind of... I guess things like apps and GUIs—I like to have that as a category because I want people to—if anyone wants to see any utilities I’ve created, that’s important to have as a page. But it might span apps, CLIs, because that’s a very big category. We have CLIs, GUIs, scripts across different categories. 

So maybe the best way to do that is to have this as the landing page, as it is, with the top levels I defined. And then a navigation bar linking to category pages by category, "Apps" as its own thing, as its own top level, and "Documentation," which we already have embedded into the website as its own page—but that’s a common one as well. So I think those are the ones I’d like to reorganize a little bit. And then in the categories page that exists currently, we have some duplication. 

As an example, there is "Indexes" and "Awesome lists," which is great, because I usually just call them "resource lists." That would be a better name, to be honest. And then we have "Awesomeness," and there's definitely no need for both. Those should be consolidated. Likewise, "MCP servers," "MCP integrations"—we should have one consolidated list of my MCP projects. So those are the combinations. And I know the process is generally—you can see how it’s documented, but it’s a pull from GitHub and Hugging Face to a backend data file, a JSON file, with a bit of filtering, and then we spread out to the category pages. 

So we might need to implement that categorization at that level as opposed to here, but let’s work on those changes.