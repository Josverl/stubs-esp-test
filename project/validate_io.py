import io

# from typing import Any, IO, Optional

alloc_size = 512


buffer = io.StringIO(alloc_size)  # type: ignore # FIXME: io.StringIO(alloc_size) valid in Micropython
buffer = io.BytesIO(alloc_size)  # type: ignore # FIXME: io.BytesIO(alloc_size) valid in Micropython
