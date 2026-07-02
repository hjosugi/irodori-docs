# ERD And Schema Designer

The ERD surface is both a browser aid and a design surface.

## Explore A Schema

Seed a diagram from a live connection to inspect tables, columns, primary keys,
foreign keys, and relationships. Move tables to make the shape readable and keep
large schemas focused on one subject area at a time.

## Design Changes

Create or edit tables, columns, keys, and relationships in the designer before
generating SQL. Forward engineering emits ordered `CREATE` and `ALTER`
statements so foreign-key dependencies are applied after the base tables exist.

## Exchange Diagrams

Export diagram JSON when sharing a design or keeping a review artifact with a
change proposal. Import JSON to continue work later or compare a proposed design
with a live connection.
