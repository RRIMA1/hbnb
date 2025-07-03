
# HBnB - Part 01: System Design and Architecture Diagrams

This directory explains the architecture contains several diagrams of the architecture and key processes of the HBNB project a copy of RBNB.
This document serves as a comprehensive blueprint for the system’s architecture, core design, and API interactions, and will guide the development and maintenance of the application going forward.
These diagrams are created using draw.io and describe the data model and interactions between different components of the system.

---

## Overview
The HBnB Evolution application allows users to:

- **Manage Users**: Register, update profiles,reserve, and assign admin privileges.
- **Manage Places**: List properties, specify details (name, price, location, amenities), and perform CRUD operations.
- **Manage Reviews**: Leave, update, delete, and view reviews on places.
- **Manage Amenities**: Create, update, delete, and list amenities to associate with places.

The documentation includes:

- High-level architectural design.
- Detailed class diagrams.
- Sequence diagrams for key API flows.

## Architecture

The system follows a **three-layered architecture**:
1. **Presentation Layer**  
   - Exposes APIs and services to clients.
   - Handles user requests and responses.

2. **Business Logic Layer**
   - Implements core models: `User`, `Place`, `Review`, `Amenity`.
   - Contains validation and business rules.

3. **Persistence Layer**
   - Manages data storage and retrieval from the database.

A **Facade Pattern** bridges the Presentation Layer to the Business Logic Layer, providing a simplified interface for the API services to interact with the system core.

## Package Diagram

 A Package Diagram that provides a high-level structural view of the HBNB application architecture and outlines the three-layer architecture:
- **Presentation Layer**
- **Business Logic Layer**
- **Persistence Layer**

## Class Diagram

- Outlines core models of the application, their attribures, methods and relationships
Captures the following entities all inheriting from `BaseModel`:
 - `User` 
 - `Place` 
 - `Review` 
 - `Amenity` 

## Sequence Diagrams

Detailing 4 different workflow:
- `POST /register`: Register user
- `POST /places`: Add a place
- `GET /places`: Search places
- `POST /reviews`: Submit a review

