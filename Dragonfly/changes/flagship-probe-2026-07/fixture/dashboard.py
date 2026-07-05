"""Read side: render current metric values for the dashboard."""


def render(store, keys):
    lines = ["%s: %s" % (key, store.get(key)) for key in keys]
    return "\n".join(lines)
