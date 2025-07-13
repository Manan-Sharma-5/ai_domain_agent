from crewai.tools import tool
from crewai_tools import SerperDevTool
import requests
import socket
import whois

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

    Args:
        domain (str): The domain name to check (e.g., "example.com", "mybusiness.ai")

    Returns:
        str: A message indicating whether the domain is available or already registered.
    """
    # --- Step 1: DomainsDB API ---
    try:
        db_res = requests.get(
            f"https://api.domainsdb.info/v1/domains/search?domain={domain}",
            timeout=5
        )
        db_data = db_res.json()
        if db_data.get("domains"):
            create_date = db_data["domains"][0].get("create_date", "unknown")
            return f"{domain} Already registered (via DomainsDB). Created on {create_date}. We will not be taking this domain."
    except Exception as e:
        # Continue to fallback methods
        pass

    # --- Step 2: DNS Resolution (socket) ---
    dns_taken = False
    try:
        socket.gethostbyname(domain)
        dns_taken = True
    except socket.gaierror:
        dns_taken = False

    # --- Step 3: WHOIS Lookup ---
    try:
        whois_data = whois.whois(domain)
        if whois_data.domain_name or dns_taken:
            return f"{domain} already Taken (via WHOIS or DNS). Do not use this domain."
    except Exception:
        if dns_taken:
            return f"{domain} already Taken (resolves via DNS but WHOIS failed). Do not use this domain."

    # --- Final Verdict ---
    return f"{domain} Available"