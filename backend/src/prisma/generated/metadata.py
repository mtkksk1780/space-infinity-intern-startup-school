from __future__ import annotations
# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# fmt: off
# -- template metadata.py.jinja --


PRISMA_MODELS: set[str] = {
    'Message',
    'User',
    'Project',
    'Submission',
    'Feedback',
}

RELATIONAL_FIELD_MAPPINGS: dict[str, dict[str, str]] = {
    'Message': {
    },
    'User': {
        'Project': 'Project',
        'Feedback': 'Feedback',
    },
    'Project': {
        'User': 'User',
        'Submission': 'Submission',
    },
    'Submission': {
        'Project': 'Project',
        'Feedback': 'Feedback',
    },
    'Feedback': {
        'User': 'User',
        'Submission': 'Submission',
    },
}

# fmt: on