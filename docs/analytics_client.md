# Analytics Client

The `AnalyticsClient` provides a comprehensive interface for managing analytics and charts in Clappia. This client enables you to create, modify, and manage chart configurations programmatically.

## Overview

Analytics in Clappia allow you to visualize data from your apps through various chart types. The AnalyticsClient allows you to:

-  Add new charts to apps
-  Remove existing charts
-  Update chart configurations
-  Reorder charts within an app

## Initialization

```python
from clappia_api_tools.client.analytics_client import AnalyticsClient

client = AnalyticsClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)
```

## Available Methods

### Add Chart

Add a new chart to an app with specified type and configuration.

```python
result = client.add_chart(
    app_id="MFX093412",
    chart_type="Bar",
    requesting_user_email_address="user@example.com",
    chart_index=0,  # Optional: position where to add the chart
    chart_title="Sales Overview"  # Optional: title for the chart
)

if result.success:
    print(f"Chart added: {result.message}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `app_id` (str): The Clappia app ID
-  `chart_type` (str): Type of chart to add
-  `requesting_user_email_address` (str): Email of the requesting user
-  `chart_index` (int, optional): Index where to add the chart
-  `chart_title` (str, optional): Title for the chart

**Valid Chart Types:**

-  `Summary` - Summary statistics
-  `Pie` - Pie chart
-  `Doughnut` - Doughnut chart
-  `Bar` - Bar chart
-  `Line` - Line chart
-  `Map` - Map visualization
-  `Geo` - Geographic chart
-  `Gantt` - Gantt chart

### Remove Chart

Remove a chart from an app by its index.

```python
result = client.remove_chart(
    app_id="MFX093412",
    chart_index=0,
    requesting_user_email_address="user@example.com"
)

if result.success:
    print(f"Chart removed: {result.message}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `app_id` (str): The Clappia app ID
-  `chart_index` (int): Index of the chart to remove
-  `requesting_user_email_address` (str): Email of the requesting user

### Update Chart

Update the configuration of an existing chart.

```python
update_data = {
    "chart_title": "Updated Sales Overview",
    "chart_configuration": {
        "dimensions": ["region", "product"],
        "metrics": ["sales_amount"],
        "filters": {"status": "active"}
    }
}

result = client.update_chart(
    app_id="MFX093412",
    chart_index=0,
    requesting_user_email_address="user@example.com",
    update_data=update_data
)

if result.success:
    print(f"Chart updated: {result.message}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `app_id` (str): The Clappia app ID
-  `chart_index` (int): Index of the chart to update
-  `requesting_user_email_address` (str): Email of the requesting user
-  `update_data` (dict): Dictionary containing the fields to update

### Reorder Chart

Move a chart to a different position within the app.

```python
result = client.reorder_chart(
    app_id="MFX093412",
    source_chart_index=0,
    target_chart_index=2,
    requesting_user_email_address="user@example.com"
)

if result.success:
    print(f"Chart reordered: {result.message}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `app_id` (str): The Clappia app ID
-  `source_chart_index` (int): Current index of the chart to move
-  `target_chart_index` (int): New index where to move the chart
-  `requesting_user_email_address` (str): Email of the requesting user

## Response Models

### ChartResponse

Returned by all chart operations:

```python
class ChartResponse(BaseResponse):
    app_id: str
    chart_index: Optional[int]
    chart_type: Optional[str]
    operation: str
```

### AnalyticsResponse

For retrieving analytics data:

```python
class AnalyticsResponse(BaseResponse):
    app_id: str
    charts: Optional[List[ChartDefinition]]
    total_charts: Optional[int]
```

### ChartDefinition

Chart definition structure:

```python
class ChartDefinition(BaseModel):
    chart_id: str
    chart_type: str
    chart_title: Optional[str]
    configuration: Optional[Dict[str, Any]]
```

## Error Handling

All methods return response objects with consistent error handling:

```python
result = client.add_chart(
    app_id="INVALID_ID",
    chart_type="InvalidType",
    requesting_user_email_address="user@example.com"
)

if not result.success:
    print(f"Error: {result.message}")
    # Handle error appropriately
```

## Complete Example

Here's a complete example showing how to manage analytics charts:

```python
from clappia_api_tools.client.analytics_client import AnalyticsClient

# Initialize client
client = AnalyticsClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)

# Add a bar chart
add_result = client.add_chart(
    app_id="MFX093412",
    chart_type="Bar",
    requesting_user_email_address="admin@company.com",
    chart_title="Sales by Region"
)

if add_result.success:
    print("Bar chart added successfully")

    # Update the chart configuration
    update_data = {
        "chart_title": "Updated Sales by Region",
        "dimensions": ["region"],
        "metrics": ["sales_amount"],
        "filters": {"status": "active"}
    }

    update_result = client.update_chart(
        app_id="MFX093412",
        chart_index=0,
        requesting_user_email_address="admin@company.com",
        update_data=update_data
    )

    if update_result.success:
        print("Chart updated successfully")

        # Add another chart
        pie_result = client.add_chart(
            app_id="MFX093412",
            chart_type="Pie",
            requesting_user_email_address="admin@company.com",
            chart_title="Product Distribution"
        )

        if pie_result.success:
            print("Pie chart added successfully")

            # Reorder charts
            reorder_result = client.reorder_chart(
                app_id="MFX093412",
                source_chart_index=1,
                target_chart_index=0,
                requesting_user_email_address="admin@company.com"
            )

            if reorder_result.success:
                print("Charts reordered successfully")
            else:
                print(f"Failed to reorder charts: {reorder_result.message}")
        else:
            print(f"Failed to add pie chart: {pie_result.message}")
    else:
        print(f"Failed to update chart: {update_result.message}")
else:
    print(f"Failed to add bar chart: {add_result.message}")
```

## Chart Configuration Examples

### Bar Chart Configuration

```python
update_data = {
    "chart_title": "Sales Performance",
    "dimensions": ["region", "product_category"],
    "metrics": ["total_sales", "order_count"],
    "filters": {
        "date_range": "last_30_days",
        "status": "completed"
    },
    "chart_options": {
        "orientation": "vertical",
        "stacked": False,
        "show_values": True
    }
}
```

### Pie Chart Configuration

```python
update_data = {
    "chart_title": "Revenue Distribution",
    "dimensions": ["product_category"],
    "metrics": ["revenue"],
    "filters": {
        "date_range": "this_year"
    },
    "chart_options": {
        "show_percentage": True,
        "show_legend": True
    }
}
```

### Line Chart Configuration

```python
update_data = {
    "chart_title": "Sales Trend",
    "dimensions": ["date"],
    "metrics": ["daily_sales"],
    "filters": {
        "date_range": "last_90_days"
    },
    "chart_options": {
        "smooth": True,
        "show_points": True,
        "fill_area": False
    }
}
```

## Best Practices

1. **Always check response success**: Verify the `success` field before proceeding
2. **Handle errors gracefully**: Implement proper error handling for failed operations
3. **Use descriptive chart titles**: Choose meaningful names for your charts
4. **Test chart configurations**: Test chart updates in a development environment first
5. **Monitor chart performance**: Keep track of chart loading times and data accuracy
6. **Validate chart types**: Ensure the chart type is appropriate for your data
7. **Consider data volume**: Large datasets may require different chart configurations

## Validation

The client includes comprehensive validation for:

-  App ID format (uppercase letters and numbers only)
-  Valid chart types
-  Required field validation
-  Email format validation
-  Chart index bounds checking

Invalid inputs will return descriptive error messages to help identify and fix issues.
