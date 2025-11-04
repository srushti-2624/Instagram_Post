from crewai import Agent
from langchain_community.chat_models import ChatOllama

class MarketingAnalysisAgents:
    def __init__(self):
        # Using free local model
        self.llm = ChatOllama(model="openhermes")

    def product_competitor_agent(self):
        return Agent(
            name="Competitor Research Agent",
            role="Analyze competitors for the product",
            goal="Research competing brands, pricing, features, and marketing strategy",
            backstory="A seasoned market analyst specializing in consumer products.",
            llm=self.llm
        )

    def strategy_planner_agent(self):
        return Agent(
            name="Marketing Strategy Planner",
            role="Plan effective marketing strategy",
            goal="Create full marketing funnel strategy for Instagram",
            backstory="Brand strategist with 10 years experience in D2C marketing.",
            llm=self.llm
        )

    def creative_content_creator_agent(self):
        return Agent(
            name="Creative Content Creator",
            role="Write Instagram captions and creatives",
            goal="Produce engaging captions, hooks, CTAs, hashtags",
            backstory="Award-winning social media creator known for high-engagement content.",
            llm=self.llm
        )

    def senior_photographer_agent(self):
        return Agent(
            name="Senior Photographer",
            role="Design photo concepts",
            goal="Create photo direction for the product image",
            backstory="Expert product photographer working with beauty brands.",
            llm=self.llm
        )

    def chief_creative_diretor_agent(self):
        return Agent(
            name="Chief Creative Director",
            role="Review and refine creative output",
            goal="Approve photography and creative direction",
            backstory="Creative lead with luxury fashion brand experience.",
            llm=self.llm
        )

    def social_media_researcher(self):
        return Agent(
            name="Social Media Trend Researcher",
            role="Trend research",
            goal="Analyze latest Instagram trends, competitor ads, and hashtags",
            backstory="Expert in social media growth and trend analysis.",
            llm=self.llm,
            verbose=True
        )

    def instagram_content_creator(self):
        return Agent(
            name="Instagram Content Creator",
            role="Write viral content",
            goal="Write engaging and viral Instagram posts",
            backstory="Specialist in social media content and audience engagement.",
            llm=self.llm,
            verbose=True
        )
