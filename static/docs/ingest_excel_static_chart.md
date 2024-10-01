
## Chart Preservation from Table Data

Using Excel, you can preserve a chart with its current data, even if you adjust or filter the underlying table. There are two main ways to achieve this: **copying and pasting the chart as a static image** or **freezing the chart by referencing a snapshot of the data**. Here's how to do both:

### Method 1: Copy the Chart as an Image
If you don't need the chart to remain dynamic and just want to preserve it as a snapshot:

1. **Create the Chart** using your data.
2. Once the chart is as you want it, **right-click** on the chart.
3. Select **Copy**.
4. Click where you want the static version of the chart (e.g., in another sheet or section of your current sheet).
5. **Right-click** and choose **Paste as Picture** (under the paste options). This will paste the chart as a non-updating image.

   - This method "freezes" the chart in its current state as a picture, so it won’t change even if the data or filters are adjusted.

### Method 2: Create a Snapshot Data Range for the Chart
If you want the chart to remain dynamic but not update based on future changes or filtering in the original table:

1. **Create a Separate Range for the Chart**:
   - Copy the relevant data from the table that you want to visualize (for example, your filtered data for multiple countries).
   - Paste this data into another part of the spreadsheet or into another sheet.
   - Use **Paste Special** to paste values only (this will prevent links to the original data).
   
2. **Create the Chart from the Snapshot**:
   - Create your chart based on this static range, rather than the original dynamic table.
   
   Now, any changes to the original table (like filters or edits) will not affect the chart, since it's based on a fixed range of data that doesn't change.

### Bonus: Using a Pivot Chart (Partial Solution)
If you're working with multiple countries and want more control, you can also consider using a **Pivot Chart**, which allows you to visualize data in different ways while keeping control over filtering. You can set up a **Pivot Table** and **Pivot Chart** based on your data, then **disable pivot table refresh** for certain situations. However, this might not fully "freeze" the chart if the pivot table is adjusted.

---

### Conclusion:
- **If you need a completely static chart**, copying the chart and pasting it as an image is your best option.
- **If you want to preserve some flexibility**, using a snapshot range is a good choice. This way, you can prevent the chart from being updated by changes in the underlying data without completely losing the ability to adjust the chart later.

## Initial Prompt
In Excel, I can create the scatter plot, but I would like to do so for a few countries. Once a chart is created, can I freeze it somehow, so the data is preserved, but if I adjust/filter the underlying table the chart is not updated? 
