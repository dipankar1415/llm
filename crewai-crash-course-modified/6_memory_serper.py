from dotenv import load_dotenv
load_dotenv()

from crewai import LLM
import os

# Check if we have the required API keys
gemini_key = os.getenv("GEMINI_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

print("🔍 Checking API Keys...")
print(f"Gemini API Key: {'✅ Set' if gemini_key else '❌ Missing'}")
print(f"Serper API Key: {'✅ Set' if serper_key else '❌ Missing'}")

# Use Gemini model
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1
)

from crewai import Agent, Task, Crew

# Import tools conditionally
try:
    from crewai_tools import SerperDevTool
    if serper_key:
        tools = [SerperDevTool()]
        print("✅ Using SerperDevTool for web search")
    else:
        tools = []
        print("⚠️  SerperDevTool disabled - no API key")
except ImportError:
    tools = []
    print("⚠️  SerperDevTool not available")

research_agent = Agent(
    role="Research Specialist",
    goal="Research interesting facts about the topic: {topic}",
    backstory="You are an expert at finding relevant and factual data.",
    tools=tools,
    verbose=True,
    llm=llm
)

writer_agent = Agent(
    role="Creative Writer",
    goal="Write a short blog summary using the research",
    backstory="You are skilled at writing engaging summaries based on provided content.",
    llm=llm,
    verbose=True,
)

task1 = Task(
    description="Find 3-5 interesting and recent facts about {topic} as of year 2025.",
    expected_output="A bullet list of 3-5 facts",
    agent=research_agent,
)

task2 = Task(
    description="Write a 100-word blog post summary about {topic} using the facts from the research.",
    expected_output="A blog post summary",
    agent=writer_agent,
    context=[task1],
)

# Create crew with memory but without embedder to avoid Google API issues
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[task1, task2],
    verbose=True,
    memory=True
)

print("\n🚀 Starting CrewAI with Memory...")
print("=" * 50)

# Run the first task
print("\n📝 Task 1: Researching 'The future of electrical vehicles'")
result1 = crew.kickoff(inputs={"topic": "The future of electrical vehicles"})
print("\n✅ Task 1 completed!")

# Run the second task (this will use memory from the first task)
print("\n📝 Task 2: Researching 'What is the revenue outlook in this sector?'")
result2 = crew.kickoff(inputs={"topic": "What is the revenue outlook in this sector?"})
print("\n✅ Task 2 completed!")

print("\n🎉 All tasks completed successfully!")
print("=" * 50)
