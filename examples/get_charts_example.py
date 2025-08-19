#!/usr/bin/env python3
"""
Example script demonstrating how to use the AnalyticsClient get_charts method.

This script shows how to:
1. Initialize the AnalyticsClient
2. Call the get_charts method
3. Handle the response and display chart information
"""

import os
import sys
from typing import Optional

# Add the parent directory to the path to import the clappia_api_tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clappia_api_tools.client.analytics_client import AnalyticsClient
from clappia_api_tools.models.response import GetAppChartsResponse


def display_charts_info(response: GetAppChartsResponse) -> None:
    """Display chart information from the response"""
    print(f"App ID: {response.app_id}")
    print(f"Operation: {response.operation}")
    print(f"Success: {response.success}")
    print(f"Message: {response.message}")
    
    if response.charts:
        print(f"\nFound {len(response.charts)} charts:")
        for i, chart in enumerate(response.charts, 1):
            print(f"\nChart {i}:")
            print(f"  ID: {chart.chart_id}")
            print(f"  Type: {chart.chart_type}")
            print(f"  Title: {chart.chart_title or 'No title'}")
            if chart.configuration:
                print(f"  Configuration: {chart.configuration}")
            else:
                print(f"  Configuration: None")
    else:
        print("\nNo charts found for this app.")


def main():
    """Main function demonstrating get_charts usage"""
    
    # Example app ID - replace with your actual app ID
    app_id = "MFX093412"  # Replace with your actual app ID
    
    # Initialize the analytics client
    # You can either set environment variables or pass parameters directly
    client = AnalyticsClient(
        # api_key="your_api_key_here",  # Uncomment and set if not using env var
        # base_url="https://your-clappia-instance.com",  # Uncomment and set if not using env var
        # timeout=30  # Optional: default is 30 seconds
    )
    
    print(f"Fetching charts for app: {app_id}")
    print("=" * 50)
    
    try:
        # Call the get_charts method
        response = client.get_charts(app_id)
        
        # Display the results
        display_charts_info(response)
        
        # Example of error handling
        if not response.success:
            print(f"\n❌ Error occurred: {response.message}")
            return 1
        
        print(f"\n✅ Successfully retrieved charts for app {app_id}")
        return 0
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        return 1


if __name__ == "__main__":
    # Set up environment variables (optional - you can also pass them to the client)
    # os.environ["CLAPPIA_API_KEY"] = "your_api_key_here"
    # os.environ["CLAPPIA_BASE_URL"] = "https://your-clappia-instance.com"
    
    exit_code = main()
    sys.exit(exit_code)
