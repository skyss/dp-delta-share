# Example app for retrieving shared data from Skyss dataplatform

## Setup

The project and its dependencies are handled with [`uv` from Astral](https://docs.astral.sh/uv/).
The previous links take you to their docs, which also include installation instructions.

After cloning the repo, run

```shell
uv sync
```

This takes care of creating a virtual environment and installs all dependencies.

## Delta-share config

In order to work, you need to download the delta-sharing configuration file and store it as `config.share` in the root directory. You will get an activation link for downloading this file from your contact person at Skyss. 

## Running commands

You can run the cli command using uv:

`uv run share.py`

This will output: 
```
Usage: share.py [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

  Tool for downloading or plotting data from Skyss share.

Options:
  --help  Show this message and exit.

Commands:
  download-table
  list-tables
  plot-table
```

### Example commands

List all tables availbles in the share: 

`uv run share.py list-tables`

Download entire sanity_reports table as a csv. By default this is stored in `data.csv` 

`uv run share.py download-table <share.schema.table>` 

Store it as excel instead: 

`uv run share.py download-table -o excel <share.schema.table>`

Plot in time colored by the reason column

`uv run share.py plot-table <share.schema.table> reason`

Plot in time colored by the vehicle_id column:

`uv run share.py plot-table <share.schema.table> vehicle_id`