# MyRoad-content

Public **path CONTENT** for [MyRoad](https://github.com/Eliot100/MyRoad): sample Grade-3 learning paths as JSON.

The platform repo (`Eliot100/MyRoad`) loads these files via:

1. `CONTENT_DIR` environment variable, or
2. git submodule / checkout at `packages/core/content`, or
3. sibling clone `../MyRoad-content` next to the MyRoad repo.

## Layout

```
grade3/*.json   # ten demo paths (math, english, physics, piano)
```

Schema: `myroad_core.content.schema.ContentPath` in the platform package.

## Clone next to MyRoad (Windows PowerShell)

```powershell
cd path\to\projects
git clone https://github.com/Eliot100/MyRoad-content.git
git clone https://github.com/Eliot100/MyRoad.git
cd MyRoad\packages\core
$env:CONTENT_DIR = (Resolve-Path ..\..\..\MyRoad-content).Path
# or: copy/link content into packages\core\content
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[api,dev]"
uvicorn myroad_core.ui.app:app --reload --port 8765
```

## License

Sample educational content for the MyRoad POC.
