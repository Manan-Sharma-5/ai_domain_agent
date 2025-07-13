# AI Domain Agent 🚀

An intelligent domain discovery agent powered by CrewAI that helps entrepreneurs and businesses find the perfect available domain names based on their business ideas and concepts.

## ✨ Features

- **Intelligent Domain Discovery**: Analyzes your business concept to suggest relevant domain names
- **Real-time Availability Checking**: Verifies domain availability using DNS resolution and WHOIS lookups
- **Multi-TLD Support**: Checks across multiple top-level domains (.com, .org, .net, etc.)
- **Business Context Understanding**: Considers your industry, target audience, and brand positioning
- **Alternative Suggestions**: Provides creative alternatives when preferred domains are taken
- **Comprehensive Analysis**: Evaluates domain suitability for SEO, branding, and memorability

## 🛠️ Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## 🚀 Usage

### Interactive Mode

Run the agent in interactive mode to describe your business and get domain suggestions:

```bash
crewai run
```

### Example Queries

Here are some sample business descriptions you can try:

```
"I'm starting a sustainable fashion brand that focuses on eco-friendly materials and ethical manufacturing. The brand will target millennials and Gen Z consumers who care about environmental impact."
```

```
"I'm launching a meal prep service for busy professionals in urban areas. We'll deliver fresh, healthy meals twice a week with customizable options for different dietary needs."
```

```
"I'm creating an online learning platform that teaches coding to kids aged 8-16 through interactive games and projects using gamification."
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
MODEL=MODELNAME
GEMINI_API_KEY=your_google_key_here
```

### Customization

You can customize the agent's behavior by modifying:

- **Agents**: Edit `src/ai_domain_agent/config/agents.yaml` to adjust agent roles and personalities
- **Tasks**: Modify `src/ai_domain_agent/config/tasks.yaml` to change task descriptions and expectations
- **Tools**: Extend `src/ai_domain_agent/tools/custom_tool.py` to add more domain checking features

## 🤖 How It Works

1. **Business Analysis**: The agent analyzes your business description to understand:
   - Industry and niche
   - Target audience
   - Brand personality
   - Key features and benefits

2. **Domain Generation**: Based on the analysis, it generates relevant domain name suggestions considering:
   - Keywords from your business description
   - Industry-specific terms
   - Brandable variations
   - SEO-friendly options

3. **Availability Checking**: Each suggested domain is checked for availability using:
   - DNS resolution
   - WHOIS database lookups
   - Multiple TLD verification

4. **Recommendations**: The agent provides:
   - Available domains ranked by suitability
   - Explanations for each recommendation
   - Alternative suggestions if preferred domains are taken
   - Branding and SEO considerations

## 📊 Example Output

```
🎯 Domain Suggestions for Your Sustainable Fashion Brand:

✅ Available Domains:
1. ecostylebrand.com - Perfect for eco-conscious fashion, memorable and brandable
2. sustainablethreads.org - Emphasizes sustainability, great for non-profit angle
3. greenwardrobe.net - Clear environmental message, easy to remember

🔍 Alternative Suggestions:
- ethicalfashionhub.com
- ecofriendlystyle.com
- sustainableclothing.co

💡 Branding Recommendations:
- Consider .com for maximum trust and memorability
- Shorter domains are better for word-of-mouth marketing
- Include sustainability keywords for SEO benefits
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
uv install --dev

# Run linting
ruff check src/
ruff format src/

# Run type checking
mypy src/
```

## 📋 Requirements

- Python 3.10+
- CrewAI
- OpenAI API key (or other LLM provider)
- python-whois
- Additional dependencies listed in `pyproject.toml`

## 📈 Roadmap

- [ ] Add support for premium domain suggestions
- [ ] Implement domain valuation estimates
- [ ] Add trademark checking capabilities
- [ ] Support for international domains (IDN)
- [ ] Integration with domain registrars for direct purchase
- [ ] Domain monitoring and alerts
- [ ] Batch domain checking from CSV files

---

**Made with ❤️ and AI** • [Report Bug](https://github.com/yourusername/ai-domain-agent/issues) • [Request Feature](https://github.com/yourusername/ai-domain-agent/issues)
