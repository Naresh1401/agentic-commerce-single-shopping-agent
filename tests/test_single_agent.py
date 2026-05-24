from single_agent import run_single_agent

def test_single_agent_calls_tools_for_milk_search():
    state = run_single_agent('Find organic milk under $5 near store_1001.')
    tools = [item.get('tool') for item in state['tool_results']]
    assert 'search_products' in tools
    assert 'get_price' in tools
    assert 'check_inventory' in tools

