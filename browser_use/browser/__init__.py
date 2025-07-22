from typing import TYPE_CHECKING

# Type stubs for lazy imports
if TYPE_CHECKING:
	from .browser import Browser, BrowserConfig
	from .context import BrowserContext, BrowserContextConfig
	from .profile import BrowserProfile
	from .session import BrowserSession

# Lazy imports mapping for heavy browser components
_LAZY_IMPORTS = {
	'Browser': ('.browser', 'Browser'),
	'BrowserConfig': ('.browser', 'BrowserConfig'),
	'BrowserContext': ('.context', 'BrowserContext'),
	'BrowserContextConfig': ('.context', 'BrowserContextConfig'),
	'BrowserProfile': ('.profile', 'BrowserProfile'),
	'BrowserSession': ('.session', 'BrowserSession'),
}


def __getattr__(name: str):
	"""Lazy import mechanism for heavy browser components."""
	if name in _LAZY_IMPORTS:
		module_path, attr_name = _LAZY_IMPORTS[name]
		try:
			from importlib import import_module

			# Use relative import for current package
			full_module_path = f'browser_use.browser{module_path}'
			module = import_module(full_module_path)
			attr = getattr(module, attr_name)
			# Cache the imported attribute in the module's globals
			globals()[name] = attr
			return attr
		except ImportError as e:
			raise ImportError(f'Failed to import {name} from {full_module_path}: {e}') from e

	raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


__all__ = ['Browser', 'BrowserConfig', 'BrowserContext', 'BrowserContextConfig', 'BrowserSession', 'BrowserProfile']
