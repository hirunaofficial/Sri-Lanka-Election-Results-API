# Sri Lanka Election Results API

An API built with Flask to provide real-time access to election results in Sri Lanka, with data fetched from the official source: elections.gov.lk. This API offers endpoints for retrieving overall, election, district, and division-specific results.

## Features

- **Overall Results**: Obtain comprehensive cumulative election results for Sri Lanka.
- **Election Results**: Access the latest results from specific elections.
- **District Results**: Retrieve detailed election outcomes categorized by individual districts.
- **Division Results**: View election results sorted by electoral divisions for more localized insights.

## API Endpoints

| Endpoint              | Method | Description                                              |
|----------------------|--------|----------------------------------------------------------|
| `/api/overall`      | GET    | Retrieve cumulative election results for Sri Lanka.      |
| `/api/election`     | GET    | Fetch the latest results from specific elections.        |
| `/api/district`     | GET    | Get detailed election results filtered by district.      |
| `/api/division`     | GET    | Access election results filtered by electoral division.   |

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for details.

### Contact

- Author: Hiruna Gallage
- Website: [hiruna.dev](https://hiruna.dev)
- Email: [hello@hiruna.dev](mailto:hello@hiruna.dev)
