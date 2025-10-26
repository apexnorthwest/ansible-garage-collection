#!/usr/bin/python
"""
Copyright 2025 Apex Northwest

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: bucket

short_description: Create or update a bucket

version_added: "0.1.0"

description: This is my longer description explaining my test module.

options:
    name:
        description:
        - The global alias (name) to assign to the bucket.
        - Mutually exclusive with id.
        required: false
        type: str
        aliases:
        - alias
    id:
        description:
        - The id of an existing bucket to update.
        - Mutually exclusive with name.
        requred: false
        type: str
    state:
        description:
        - Desired state of the bucket:
        - If set to present, we will attempt to find a bucket with either the id or alias given.
        - If set to present and neither id nor alias are given, then we will create a new bucket always.
        - If set to absent, it will always delete any bucket with the id specified, or the bucket with the given alias.
        - Even if the bucket has one or more aliases set, it will delete all of them along with the bucket.
        required: true
        default: present
        type: str

author:
    - Tyler Bevan <tyler.bevan@apexnorthwest.com>
'''

EXAMPLES = r'''
# Create a new bucket
- name: Create a bucket named my-bucket
  apexnorthwest.garage.bucket:
    alias: "my-bucket"
    state: present

- name: Delete a bucket by id
  apexnorthwest.garage.bucket:
    id: "2a1097780e171296dcfb3776cecc919ac33a19780f8a7e814833211ada961243"
    state: absent

- name: Delete a bucket by alias
  apexnorthwest.garage.bucket:
    name: "my-bucket"
    state: absent
'''

RETURN = r'''
id:
    description: The unique id of the bucket
    type: str
    returned: always
    sample: '2a1097780e171296dcfb3776cecc919ac33a19780f8a7e814833211ada961243'
aliases:
    description: The global aliases assigned to this bucket
    type: list[str]
    returned: always
    sample: ["my-bucket"]
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        id=dict(type='str', required=False, default=False),
        name=dict(type='str', required=False, default=False, aliases=["alias"]),
        state=dict(type='str', default="present", choices=["present", "absent"])
    )

    result = dict(
        changed=False,
        id='',
        aliases=[]
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # TODO: Get bucket to see if it already exists by id

    # TODO; Get bucket by alias if id not given

    if module.check_mode:
        if bucket is None:
            result['changed'] = True
            result['id'] = ''
            if module.params['name'] is not None:
                result['aliases'].append(module.params['name'])
        elif module.params['state'] == 'absent':
            result['changed'] = True
        module.exit_json(**result)

    # TODO: Create new bucket when id not found

    # TODO: Delete found bucket if state=absent

    if changed:
        result['changed'] = True

    if errored:
        module.fail_json(msg='Something went wrong', **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
