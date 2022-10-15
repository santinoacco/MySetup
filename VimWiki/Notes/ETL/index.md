# ETL notes

## Constructing a Dataset

1. Collect the raw data.
2. Identify features & labels sources.
3. Select a sampling strategy.
4. Split the data.

- How do you measure your data set's quality & improve it?
    - Reliabiilty:
        - Degree to which you can *trust* your data. Ask & answer the following questions:
            - How common are label errors?
            - How much noise are in the features?
            - Is the data properly filtered for your problem?
        - Unreliability synthoms:
            - Omitted values.
            - Duplicated examples
            - Bad labels.
            - Bad feature values.
    - Feature representation: mapping of data to useful features. Consider:
        - How is data shown to the model?
        - Show you normalize numeric values?
        - What is your policy to handle outliers & annomalies?
    - Minimizing skew:
        - Consider features available at production level.
        - Account for time bottlenecks in prediction & ingestion.
        - Is the training set *representative* of the production set?
- How much data do you need to get useful results?
    - Rule of thumb: train on at least an order of magnitude more examples than trainable parameters.

Types of Logs:

- Transactional logs: record a specific event.
- Attribute data: contains snapshots of information. ex; search history at time of query
- Aggregate statistics: create an attribute from multiple transactional logs.
