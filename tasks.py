from crewai import Task
from textwrap import dedent

class MarketingAnalysisTasks:
	def product_analysis(self, agent, product_website, product_details):
		return Task(
			description=dedent(f"""
				Analyze the given product website: {product_website}.
				Extra details provided by the customer: {product_details}.

				Focus on identifying unique features, benefits,
				and the overall narrative presented.

				Your final report should clearly articulate the
				product's key selling points, its market appeal,
				and suggestions for enhancement or positioning.
			"""),
			expected_output="Detailed product analysis including target audience, USPs, and improvements.",
			agent=agent
		)

	def competitor_analysis(self, agent, product_website, product_details):
		return Task(
			description=dedent(f"""
				Explore competitors of: {product_website}.
				Extra details: {product_details}.

				Identify the top 3 competitors and analyze positioning,
				strategy, and their strengths vs weaknesses.
			"""),
			expected_output="List of 3 competitors with full comparison and marketing insights.",
			agent=agent
		)

	def campaign_development(self, agent, product_website, product_details):
		return Task(
			description=dedent(f"""
				Create a targeted Instagram marketing campaign for: {product_website}
				Details: {product_details}

				Provide content strategy, angles, and hooks that would convert.
			"""),
			expected_output="Instagram campaign plan with 5 creative ideas & hooks.",
			agent=agent
		)

	def instagram_ad_copy(self, agent):
		return Task(
			description=dedent("""
				Write 3 Instagram caption variations.
			"""),
			expected_output="Three engaging Instagram captions with CTAs and hashtags.",
			agent=agent
		)

	def take_photograph_task(self, agent, copy, product_website, product_details):
		return Task(
			description=dedent(f"""
				Generate 3 creative photography ideas inspired by this copy:
				{copy}
			"""),
			expected_output="Three imaginative photo concepts in stylized prompt format.",
			agent=agent
		)

	def review_photo(self, agent, product_website, product_details):
		return Task(
			description=dedent(f"""
				Review and refine the 3 photo prompts for the campaign.
			"""),
			expected_output="Three polished & improved final Midjourney prompts.",
			agent=agent
		)
