from hr_blog_writer.agents import research_agent, planner_agent, writer_agent, seo_agent, review_agent
from hr_blog_writer.utils import seo_utils

def run_pipeline():
    # Step 1: Get a trending HR topic
    topic = research_agent.get_trending_topic()
    print(f"Topic: {topic}")

    # Step 2: Gather research text (was incorrectly called `get_research_text`)
    research = research_agent.gather_information(topic)
    research_text = "\n\n".join(research)
    print("Research text collected.")

    # Step 3: Generate outline
    outline = planner_agent.generate_outline(topic)
    print("Outline generated.")

    # Step 4: Generate blog content
    content = writer_agent.generate_blog(outline, research_text)
    print("Content generated.")

    # Step 5: Optimize for SEO
    seo_content = seo_agent.optimize_for_seo(content)
    print("Content optimized for SEO.")

    # Step 6: Final proofreading and improvements
    final_content = review_agent.proofread_and_improve(seo_content)
    print("Content reviewed and finalized.")

    # Step 7: Save to file
    with open("output_blog.txt", "w", encoding="utf-8") as f:
        f.write(final_content)

if __name__ == "__main__":
    run_pipeline()
