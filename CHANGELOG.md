# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2025-10-15
### Added
- Add final report notebook

## [0.1.1] - 2025-10-15
### Added
- Add demo notebook

## [0.1.0] - 2025-10-15
### Added
- Add iterator support for `EventList` and `LinkedEventList`
- Add getitem indexing and slicing support for `EventList` and `LinkedEventList`
- Add utils for storing general helper functions
- Add setitem support for `EventList` and `LinkedEventList`
- Add copy method to `EventNode` to avoid node conflicts'
- Add unit testing

### Changed
- Major refactoring to consolidate various changes from Dnyanada's search algorithm implementation, Augustine's class definitions, and Stephanie's prototype tool
- Generalize search and sort algorithms to apply to any iterable

## [0.0.0] - 2025-10-04

### Added
- Add general project structure
- Add `Event` and `EventNode` classes for establishing two unique data types
- Add `EventList` and `LinkedEventList` classes for storing events
- Add `SortingAlgorithm` class and associated functions for defining different ways to sort an event list using the `sort_data` function
- Add `SearchAlgorithm` class and associated functions for defining different ways to search an event list for a specific ID using the `search_data` function

### Changed
- Update README.md