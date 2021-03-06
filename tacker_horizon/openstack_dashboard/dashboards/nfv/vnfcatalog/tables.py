# Copyright 2015 Brocade Communications System, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables

from openstack_dashboard import policy

class MyFilterAction(tables.FilterAction):
    name = "myfilter"

class DeleteVNFLink(policy.PolicyTargetMixin, tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Delete VNF",
            u"Delete VNF",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Delete VNF",
            u"Delete VNF",
            count
        )

class OnBoardVNFLink(tables.LinkAction):
    name = "onboardvnf"
    verbose_name = _("Onboard VNF")
    classes = ("ajax-modal",)
    icon = "plus"
    url = "horizon:nfv:vnfcatalog:onboardvnf"


class VNFCatalogTable(tables.DataTable):
    name = tables.Column('name', \
                         verbose_name=_("Name"))
    description = tables.Column('description', \
                           verbose_name=_("Description"))
    services = tables.Column('services', \
                         verbose_name=_("Services"))
    id = tables.Column('id', \
                         verbose_name=_("Catalog Id"))

    class Meta:
        name = "vnfcatalog"
        verbose_name = _("VNFCatalog")
        table_actions = (OnBoardVNFLink, DeleteVNFLink, MyFilterAction,)
