E-Commerce Analytics Lakehouse Platform
Project Overview

This project builds a scalable end-to-end data platform for an e-commerce company using Databricks Lakehouse Architecture. The platform ingests customer, product, order, payment, and shipment data from multiple sources, processes it through a Medallion Architecture (Bronze, Silver, Gold), and provides analytical datasets for business reporting and dashboarding.

The primary objectives are:

Track customer purchasing behavior
Analyze sales performance
Monitor order fulfillment
Evaluate product performance
Generate business KPIs
Support executive dashboards
Business Problem

The company receives data from multiple operational systems:

Customer Management System
Order Management System
Product Catalog
Payment Gateway
Shipment Tracking System

The business faces challenges such as:

Duplicate customer records
Delayed shipment updates
Missing product information
Inconsistent data formats
Slow reporting performance

The goal is to create a centralized and reliable analytics platform.

Source Systems
Customers
customer_id
first_name
last_name
email
phone
city
state
country
registration_date
updated_at
Products
product_id
product_name
category
brand
price
inventory_quantity
updated_at
Orders
order_id
customer_id
order_date
order_status
total_amount
updated_at
Order Items
order_item_id
order_id
product_id
quantity
unit_price
Payments
payment_id
order_id
payment_method
payment_status
payment_date
amount
Shipments
shipment_id
order_id
shipment_status
carrier
shipment_date
delivery_date
updated_at
Architecture
Source Systems
       ↓
Auto Loader
       ↓
Bronze Layer
       ↓
Data Quality & Deduplication
       ↓
Silver Layer
       ↓
Business Aggregations
       ↓
Gold Layer
       ↓
Power BI Dashboard
