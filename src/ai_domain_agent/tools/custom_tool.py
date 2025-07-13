from crewai.tools import tool
from crewai_tools import SerperDevTool
import whois
import socket

@tool
def keyword_research_tool(query: str) -> str:
    """
    A tool for performing keyword research using Serper API.
    Focus on industry-specific terms, competitors, and brandable concepts.
    
    Args:
        query (str): The search query for keyword research (e.g., "fintech startups", "AI competitors", "SaaS pricing models")
        
    Returns:
        str: Formatted research results with keywords, trends, and competitive insights.
        
    Example:
        keyword_research_tool("AI LLMs")
        This will return a list of relevant keywords, trends, and competitive insights related to AI LLMs.
    """
    serper_tool = SerperDevTool()
    results = serper_tool._run(query=query)
    return results

@tool
def domain_availability_checker(domain: str) -> str:
    """
        Check if a domain name is available for registration or already taken.
        This tool performs DNS resolution and WHOIS lookup to determine domain status. 
        Use this when you need to verify domain availability for website projects, 
        business planning, or domain investment decisions.
        
    Args:
        domain (str): The domain name to check (e.g., "example.com", "mybusiness.ai")
        
    Returns:
        str: A message indicating whether the domain is available or already registered.
    """
    try:
        # First check if domain resolves
        socket.gethostbyname(domain)
        domain_resolves = True
    except socket.gaierror:
        domain_resolves = False
    
    try:
        whois_info = whois.whois(domain)
        
        # Check if any registration info exists
        if (whois_info.creation_date or 
            whois_info.registrar or 
            whois_info.registrant or
            domain_resolves):
            return f"The domain '{domain}' is already registered."
        else:
            return f"The domain '{domain}' appears to be available."
            
    except:
        if domain_resolves:
            return f"The domain '{domain}' is registered (resolves but WHOIS failed)."
        else:
            return f"The domain '{domain}' appears to be available."
