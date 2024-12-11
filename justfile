go:
   openapi-generator-cli generate -i deezer.yaml -g python
   uvx poetry2uv; mv pyproject_transformed.toml pyproject.toml; clear;  uv run main.py


clean:
  rm -rf openapi_client test docs openapi_client.egg-info
